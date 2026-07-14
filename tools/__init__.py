"""CausalSentinel tools package - each function is one 'tool' the agent can call.

The function docstring is what the model reads to decide WHEN to call the tool, and
the type hints define the arguments. So: clear docstrings + type hints = better agent.
"""
# Round 1
from .uniprot import get_uniprot_dossier
from .opentargets import get_target_disease_evidence
from .chembl import get_chembl_modulators
from .mr import get_mr_result
# Round 2
from .clinvar import get_clinvar_variants
from .gnomad import get_gnomad_constraint
from .gwas import get_gwas_catalog
from .pharmgkb import get_pharmgkb_drug_gene

ROUND1_TOOLS = [
    get_uniprot_dossier,
    get_target_disease_evidence,
    get_chembl_modulators,
    get_mr_result,
]

# All active tools wired into the agent (Round 1 + Round 2 = 7 live + 1 MR stub).
TOOLS = ROUND1_TOOLS + [
    get_clinvar_variants,
    get_gnomad_constraint,
    get_gwas_catalog,
    get_pharmgkb_drug_gene,
]
