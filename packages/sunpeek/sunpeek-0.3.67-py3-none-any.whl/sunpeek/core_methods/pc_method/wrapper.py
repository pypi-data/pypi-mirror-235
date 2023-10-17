import warnings
from typing import List
import datetime as dt
import itertools

from sunpeek.common.utils import sp_logger
from sunpeek.components import Plant
from sunpeek.components.base import AlgoCheckMode
from sunpeek.core_methods import CoreAlgorithm, CoreStrategy
from sunpeek.serializable_models import ProblemReport, PCMethodProblem
from sunpeek.core_methods.pc_method.main import PCMethod
from sunpeek.core_methods.pc_method import PCFormulae, PCMethods
from sunpeek.core_methods.common.main import AlgoResult


def run_performance_check(plant: Plant,
                          method: List[PCMethods | str | None] | None = None,
                          formula: List[PCFormulae | int | None] | None = None,
                          use_wind: List[None | bool] | None = None,
                          # Context
                          eval_start: dt.datetime | None = None,
                          eval_end: dt.datetime | None = None,
                          # Settings:
                          safety_pipes: float | None = None,
                          safety_uncertainty: float | None = None,
                          safety_others: float | None = None,
                          interval_length: dt.timedelta | None = None,
                          min_data_in_interval: int | None = None,
                          max_gap_in_interval: dt.timedelta | None = None,
                          max_nan_density: float | None = None,
                          min_intervals_in_output: int | None = None,
                          check_accuracy_level: str | None = None,
                          ) -> AlgoResult:
    """Run Performance Check analysis with given settings, trying all possible strategies in order.
    """
    plant.check_interval(eval_start, eval_end, method_name='Performance Check analysis')

    kwds = {
        'safety_pipes': safety_pipes,
        'safety_uncertainty': safety_uncertainty,
        'safety_others': safety_others,
        'interval_length': interval_length,
        'min_data_in_interval': min_data_in_interval,
        'max_gap_in_interval': max_gap_in_interval,
        'max_nan_density': max_nan_density,
        'min_intervals_in_output': min_intervals_in_output,
        'check_accuracy_level': check_accuracy_level,
    }
    pc_algo = PCAlgo(plant, methods=method, formulae=formula, use_wind=use_wind, **kwds)
    algo_result = pc_algo.run()
    return algo_result


def get_pc_problemreport(plant: Plant,
                         method: List[PCMethods | str | None] | None = None,
                         formula: List[PCFormulae | int | None] | None = None,
                         use_wind: List[bool | None] | None = None,
                         # Settings:
                         safety_pipes: float | None = None,
                         safety_uncertainty: float | None = None,
                         safety_others: float | None = None,
                         interval_length: dt.timedelta | None = None,
                         min_data_in_interval: int | None = None,
                         max_gap_in_interval: dt.timedelta | None = None,
                         max_nan_density: float | None = None,
                         min_intervals_in_output: int | None = None,
                         check_accuracy_level: str | None = None,
                         ) -> ProblemReport:
    """Report which strategies of the Performance Check analysis can be run for given plant config and settings.
    Does not actually run PC calculation. Can operate on a plant without data uploaded.
    """
    kwds = {
        'safety_pipes': safety_pipes,
        'safety_uncertainty': safety_uncertainty,
        'safety_others': safety_others,
        'interval_length': interval_length,
        'min_data_in_interval': min_data_in_interval,
        'max_gap_in_interval': max_gap_in_interval,
        'max_nan_density': max_nan_density,
        'min_intervals_in_output': min_intervals_in_output,
        'check_accuracy_level': check_accuracy_level,
    }

    pc_algo = PCAlgo(plant, methods=method, formulae=formula, use_wind=use_wind, **kwds)
    return pc_algo.get_config_problems()


def list_pc_problems(plant: Plant,
                     method: List[PCMethods | str | None] | None = None,
                     formula: List[PCFormulae | int | None] | None = None,
                     use_wind: List[bool | None] | None = None,
                     ) -> List[PCMethodProblem]:
    """Report which strategies of the Performance Check analysis can be run for given plant config and settings.
    Does not actually run PC calculation. Can operate on a plant without data uploaded.
    """
    pc_algo = PCAlgo(plant, methods=method, formulae=formula, use_wind=use_wind)
    out = []
    for strategy in pc_algo.strategies:
        report = strategy.get_problem_report(AlgoCheckMode.config_only)
        out.append(PCMethodProblem(strategy.pc.mode.value,
                                   strategy.pc.formula.id,
                                   strategy.pc.formula.use_wind,
                                   report.success,
                                   report.parse()))
    return out


class PCStrategy(CoreStrategy):
    def __init__(self, pc: PCMethod):
        super().__init__(pc.plant)
        self.pc = pc
        self.name = (f'Thermal Power Check with '
                     f'Mode: {pc.mode.value}, '
                     f'Formula: {pc.formula.id}, '
                     f'{"Using wind" if pc.formula.use_wind else "Ignoring wind"}')

    def _calc(self):
        return self.pc.run()  # results.PCMethodOutput

    def _report_problems(self, check_mode: AlgoCheckMode) -> ProblemReport:
        return self.pc.report_problems(check_mode)


class PCAlgo(CoreAlgorithm):

    def define_strategies(self, methods=None, formulae=None, use_wind=None, **kwargs) -> List[PCStrategy]:
        """Returns list of all possible PC method strategies in the order they will be executed.
        """
        variants = {'methods': self.create_variants(methods, allowed_type=PCMethods,
                                                    default=[PCMethods.iso, PCMethods.extended]),
                    'formulae': self.create_variants(formulae, allowed_type=PCFormulae,
                                                     default=[PCFormulae.two, PCFormulae.one, PCFormulae.three]),
                    'wind': self.create_variants(use_wind, allowed_type=bool, default=[True, False])}
        all_variants = list(itertools.product(*variants.values()))
        strategies = [PCStrategy(PCMethod.create(self.component, m, f, w, **kwargs)) for m, f, w in all_variants]

        return strategies


def get_pc_successful_strategy(plant: Plant,
                               method: List[PCMethods | str | None] | None = None,
                               formula: List[PCFormulae | int | None] | None = None,
                               use_wind: List[bool | None] | None = None,
                               # Settings:
                               safety_pipes: float | None = None,
                               safety_uncertainty: float | None = None,
                               safety_others: float | None = None,
                               interval_length: dt.timedelta | None = None,
                               min_data_in_interval: int | None = None,
                               max_gap_in_interval: dt.timedelta | None = None,
                               max_nan_density: float | None = None,
                               min_intervals_in_output: int | None = None,
                               check_accuracy_level: str | None = None,
                               ) -> PCStrategy:
    """Report the first strategy of the Performance Check analysis that is successful with given plant and
    settings. Like `get_pc_problemreport()`, this does not actually run calculations.
    """
    kwds = {
        'safety_pipes': safety_pipes,
        'safety_uncertainty': safety_uncertainty,
        'safety_others': safety_others,
        'interval_length': interval_length,
        'min_data_in_interval': min_data_in_interval,
        'max_gap_in_interval': max_gap_in_interval,
        'max_nan_density': max_nan_density,
        'min_intervals_in_output': min_intervals_in_output,
        'check_accuracy_level': check_accuracy_level,
    }

    pc_algo = PCAlgo(plant, methods=method, formulae=formula, use_wind=use_wind, **kwds)
    strategy = pc_algo.successful_strategy

    return strategy  # noqa
