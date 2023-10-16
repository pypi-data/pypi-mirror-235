from __future__ import annotations

import warnings
from dataclasses import dataclass, replace
from typing import List, Optional, Union

import pharmpy.tools.iivsearch.algorithms as algorithms
from pharmpy.deps import pandas as pd
from pharmpy.internals.fn.signature import with_same_arguments_as
from pharmpy.internals.fn.type import with_runtime_arguments_type_check
from pharmpy.model import Model
from pharmpy.modeling import (
    add_pd_iiv,
    add_pk_iiv,
    calculate_bic,
    create_joint_distribution,
    has_random_effect,
)
from pharmpy.tools import summarize_modelfit_results
from pharmpy.tools.common import RANK_TYPES, ToolResults, create_results, update_initial_estimates
from pharmpy.tools.iivsearch.algorithms import _get_fixed_etas
from pharmpy.tools.modelfit import create_fit_workflow
from pharmpy.workflows import Task, Workflow, WorkflowBuilder, call_workflow
from pharmpy.workflows.results import ModelfitResults

IIV_STRATEGIES = frozenset(
    ('no_add', 'add_diagonal', 'fullblock', 'pd_add_diagonal', 'pd_fullblock')
)
IIV_ALGORITHMS = frozenset(('brute_force',) + tuple(dir(algorithms)))


def create_workflow(
    algorithm: str,
    iiv_strategy: str = 'no_add',
    rank_type: str = 'bic',
    cutoff: Optional[Union[float, int]] = None,
    results: Optional[ModelfitResults] = None,
    model: Optional[Model] = None,
    keep: Optional[List[str]] = None,
):
    """Run IIVsearch tool. For more details, see :ref:`iivsearch`.

    Parameters
    ----------
    algorithm : str
        Which algorithm to run (brute_force, brute_force_no_of_etas, brute_force_block_structure)
    iiv_strategy : str
        If/how IIV should be added to start model. Possible strategies are 'no_add', 'add_diagonal',
        or 'fullblock'. Default is 'no_add'
    rank_type : str
        Which ranking type should be used (OFV, AIC, BIC, mBIC). Default is BIC
    cutoff : float
        Cutoff for which value of the ranking function that is considered significant. Default
        is None (all models will be ranked)
    results : ModelfitResults
        Results for model
    model : Model
        Pharmpy model
    keep :  List[str]
        List of IIVs to keep

    Returns
    -------
    IIVSearchResults
        IIVsearch tool result object

    Examples
    --------
    >>> from pharmpy.modeling import *
    >>> from pharmpy.tools import run_iivsearch, load_example_modelfit_results
    >>> model = load_example_model("pheno")
    >>> results = load_example_modelfit_results("pheno")
    >>> run_iivsearch('brute_force', results=results, model=model)   # doctest: +SKIP
    """

    wb = WorkflowBuilder(name='iivsearch')
    start_task = Task('start_iiv', start, model, algorithm, iiv_strategy, rank_type, cutoff, keep)
    wb.add_task(start_task)
    task_results = Task('results', _results)
    wb.add_task(task_results, predecessors=[start_task])
    return Workflow(wb)


def create_step_workflow(input_model, base_model, wf_algorithm, iiv_strategy, rank_type, cutoff):
    wb = WorkflowBuilder()
    start_task = Task(f'start_{wf_algorithm.name}', _start_algorithm, base_model)
    wb.add_task(start_task)

    if iiv_strategy != 'no_add':
        wf_fit = create_fit_workflow(n=1)
        wb.insert_workflow(wf_fit)
        base_model_task = wf_fit.output_tasks[0]
    else:
        base_model_task = start_task

    wb.insert_workflow(wf_algorithm)

    task_result = Task('results', post_process, rank_type, cutoff, input_model, base_model.name)

    post_process_tasks = [base_model_task] + wb.output_tasks
    wb.add_task(task_result, predecessors=post_process_tasks)

    return Workflow(wb)


def start(context, input_model, algorithm, iiv_strategy, rank_type, cutoff, keep):
    if iiv_strategy != 'no_add':
        model_iiv = input_model.replace(name='base_model')
        model_iiv = update_initial_estimates(model_iiv)
        base_model = _add_iiv(iiv_strategy, model_iiv)
        base_model = algorithms.update_description(base_model)
    else:
        base_model = input_model

    if algorithm == 'brute_force':
        list_of_algorithms = ['brute_force_no_of_etas', 'brute_force_block_structure']
    else:
        list_of_algorithms = [algorithm]
    sum_tools, sum_models, sum_inds, sum_inds_count, sum_errs = [], [], [], [], []

    models = []
    models_set = set()
    last_res = None
    final_model = None

    sum_models = [summarize_modelfit_results(input_model.modelfit_results)]

    for algorithm_cur in list_of_algorithms:
        algorithm_func = getattr(algorithms, algorithm_cur)
        if algorithm_cur == "brute_force_no_of_etas":
            wf_algorithm = algorithm_func(base_model, index_offset=len(models_set), keep=keep)
        else:
            wf_algorithm = algorithm_func(base_model, index_offset=len(models_set))

        wf = create_step_workflow(
            input_model, base_model, wf_algorithm, iiv_strategy, rank_type, cutoff
        )
        res = call_workflow(wf, f'results_{algorithm}', context)
        # NOTE: Append results
        new_models = list(filter(lambda model: model.name not in models_set, res.models))
        models.extend(new_models)
        models_set.update(model.name for model in new_models)

        if base_model.name in sum_models[-1].index.values:
            summary_models = res.summary_models.drop(base_model.name, axis=0)
        else:
            summary_models = res.summary_models

        sum_tools.append(res.summary_tool)
        sum_models.append(summary_models)
        sum_inds.append(res.summary_individuals)
        sum_inds_count.append(res.summary_individuals_count)
        sum_errs.append(res.summary_errors)

        final_model = next(
            filter(lambda model: model.name == res.final_model.name, res.models), base_model
        )

        base_model = final_model
        iiv_strategy = 'no_add'
        last_res = res

        assert base_model is not None
        if (
            len(set(base_model.random_variables.iiv.names).difference(_get_fixed_etas(base_model)))
            <= 1
        ):
            break

    assert last_res is not None
    assert final_model is not None

    res_modelfit_input = input_model.modelfit_results
    res_modelfit_final = final_model.modelfit_results

    # NOTE: Compute final final model
    final_final_model = last_res.final_model
    if res_modelfit_input and res_modelfit_final:
        bic_input = calculate_bic(input_model, res_modelfit_input.ofv, type='iiv')
        bic_final = calculate_bic(final_model, res_modelfit_final.ofv, type='iiv')
        if bic_final > bic_input:
            warnings.warn(
                f'Worse {rank_type} in final model {final_model.name} '
                f'({bic_final}) than {input_model.name} ({bic_input}), selecting '
                f'input model'
            )
            final_final_model = input_model

    keys = list(range(1, len(list_of_algorithms) + 1))

    return IIVSearchResults(
        summary_tool=_concat_summaries(sum_tools, keys),
        summary_models=_concat_summaries(sum_models, [0] + keys),  # To include input model
        summary_individuals=_concat_summaries(sum_inds, keys),
        summary_individuals_count=_concat_summaries(sum_inds_count, keys),
        summary_errors=_concat_summaries(sum_errs, keys),
        final_model=final_final_model,
        models=models,
        tool_database=last_res.tool_database,
    )


def _concat_summaries(summaries, keys):
    return pd.concat(summaries, keys=keys, names=['step'])


def _results(res):
    return res


def _start_algorithm(model):
    model = model.replace(parent_model=model.name)
    return model


def _add_iiv(iiv_strategy, model):
    assert iiv_strategy in ['add_diagonal', 'fullblock', 'pd_add_diagonal', 'pd_fullblock']
    if iiv_strategy in ['add_diagonal', 'fullblock']:
        model = add_pk_iiv(model)
        if iiv_strategy == 'fullblock':
            model = create_joint_distribution(
                model, individual_estimates=model.modelfit_results.individual_estimates
            )
    elif iiv_strategy in ['pd_add_diagonal', 'pd_fullblock']:
        model = add_pd_iiv(model)
        if iiv_strategy == 'pd_fullblock':
            model = create_joint_distribution(
                model, individual_estimates=model.modelfit_results.individual_estimates
            )
    return model


def post_process(rank_type, cutoff, input_model, base_model_name, *models):
    res_models = []
    base_model = None
    for model in models:
        if model.name == base_model_name:
            base_model = model
        else:
            res_models.append(model)

    assert len(res_models) > 0

    if not base_model:
        raise ValueError('Error in workflow: No base model')

    # In order to have the IIV structure of the input model in the description column
    # in the result summaries
    if input_model.name == base_model.name:
        base_model = algorithms.update_description(base_model)

    res = create_results(
        IIVSearchResults, input_model, base_model, res_models, rank_type, cutoff, bic_type='iiv'
    )

    summary_tool = res.summary_tool
    assert summary_tool is not None
    summary_models = summarize_modelfit_results([model.modelfit_results for model in models])

    return replace(res, summary_models=summary_models)


@with_runtime_arguments_type_check
@with_same_arguments_as(create_workflow)
def validate_input(
    algorithm,
    iiv_strategy,
    rank_type,
    model,
    keep,
):
    if algorithm not in IIV_ALGORITHMS:
        raise ValueError(
            f'Invalid `algorithm`: got `{algorithm}`, must be one of {sorted(IIV_ALGORITHMS)}.'
        )

    if rank_type not in RANK_TYPES:
        raise ValueError(
            f'Invalid `rank_type`: got `{rank_type}`, must be one of {sorted(RANK_TYPES)}.'
        )

    if iiv_strategy not in IIV_STRATEGIES:
        raise ValueError(
            f'Invalid `iiv_strategy`: got `{iiv_strategy}`,'
            f' must be one of {sorted(IIV_STRATEGIES)}.'
        )

    if keep:
        for parameter in keep:
            try:
                has_random_effect(model, parameter, "iiv")
            except KeyError:
                raise ValueError(f"Parameter {parameter} has no iiv.")


@dataclass(frozen=True)
class IIVSearchResults(ToolResults):
    pass
