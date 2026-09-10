from dataclasses import dataclass
import json

@dataclass(frozen=True)
class Application:
    applicant: str; property_value: float; loan_amount: float; annual_income: float; monthly_debt: float; term_years: int

def assess(application: Application):
    ltv = application.loan_amount / application.property_value
    lti = application.loan_amount / application.annual_income
    monthly_income = application.annual_income / 12
    dti = application.monthly_debt / monthly_income
    checks = {"ltv_within_policy": ltv <= .90, "lti_within_policy": lti <= 4.0, "dti_within_policy": dti <= .35}
    decision = "ELIGIBLE" if all(checks.values()) else "MANUAL_REVIEW"
    return {"ltv":round(ltv,3),"lti":round(lti,2),"dti":round(dti,3),"checks":checks,"decision":decision}

def missing_documents(received):
    required = {"identity","income","bank_statements","property_valuation"}
    return sorted(required - set(received))

if __name__ == "__main__":
    case = Application("Sample Applicant",420000,330000,92000,650,30)
    print(json.dumps({"assessment":assess(case),"missing":missing_documents(["identity","income"])},indent=2))

