from datetime import datetime
from src.challenges.base_challenge import IChallenge
from core.validators import BenefitsInput, BenefitsOutput


class BenefitsChallenge(IChallenge):
    """
    Challenge implementation for calculating employment benefits.

    This class handles the calculation of proportional vacation pay and
    thirteenth salary (Christmas bonus) according to Brazilian labor laws.
    Calculations are based on the CLT (Consolidação das Leis do Trabalho)
    rules.

    Inherits from:
        IChallenge: Base interface for challenge implementations
    """

    def execute(self, input_data: BenefitsInput) -> BenefitsOutput:
        """
        Calculate employment benefits based on salary and employment period.

        Args:
            input_data (BenefitsInput): Input data containing:
                - salary (float): Monthly salary amount
                - hire_date (date): Employee hire date
                - resignation_date (date):
                    Employee resignation/termination date

        Returns:
            BenefitsOutput: Object containing calculated benefits:
                - vacation (float): Proportional vacation pay value
                - thirteenth_salary (float): Proportional thirteenth
                salary value

        Calculation Details:
            - Vacation: Proportional calculation based on worked days since
            last anniversary
            - Thirteenth Salary: Proportional calculation based on months
            worked in the year (considers full month if more
            than 15 days worked)

        Note:
            Calculations follow Brazilian labor law (CLT) requirements and use
            30-day months for daily salary calculation as standard practice.
        """
        salary = input_data.salary
        hire_date = datetime.combine(input_data.hire_date, datetime.min.time())
        resignation_date = datetime.combine(
            input_data.resignation_date, datetime.min.time()
        )

        # Salário diário (baseado em 30 dias, média usada para férias)
        daily_salary = salary / 30

        # Calcular férias proporcionais
        last_anniversary = datetime(
            resignation_date.year
            if hire_date.replace(year=hire_date.year) <= resignation_date
            else hire_date.year,
            hire_date.month,
            hire_date.day,
        )
        if last_anniversary > resignation_date:
            last_anniversary = last_anniversary.replace(year=last_anniversary.year - 1)
        days_worked = (resignation_date - last_anniversary).days
        is_leap_year = last_anniversary.year % 4 == 0 and (
            last_anniversary.year % 100 != 0 or last_anniversary.year % 400 == 0
        )
        year_days = 366 if is_leap_year and last_anniversary.month <= 2 else 365
        vacation_proportion = min(days_worked / year_days, 1.0)
        vacation_days = 30 * vacation_proportion
        vacation_value = round(
            vacation_days * daily_salary, 2
        )  # Arredonda para 2 casas decimais

        # Calcular décimo terceiro proporcional
        # (conforme CLT: mês completo se > 15 dias)
        year_start = datetime(resignation_date.year, 1, 1)
        days_worked_in_year = (
            resignation_date - year_start
        ).days + 1  # Inclui o dia da demissão
        months_worked = (
            days_worked_in_year + 14
        ) // 30  # Arredonda para mês completo se > 15 dias
        months_worked = min(months_worked, 12)  # Limita a 12 meses
        thirteenth_proportion = months_worked / 12
        thirteenth_value = round(
            salary * thirteenth_proportion, 2
        )  # Arredonda para 2 casas decimais

        return BenefitsOutput(
            vacation=vacation_value, thirteenth_salary=thirteenth_value
        )
