from src.app import Application, assess, missing_documents
def test_policy_decision(): assert assess(Application("Sample",400000,300000,90000,500,30))["decision"]=="ELIGIBLE"
def test_document_gap(): assert "property_valuation" in missing_documents(["identity","income","bank_statements"])

