"""CausalSentinel tools package - each function is one 'tool' the agent can call.

The function docstring is what the model reads to decide WHEN to call the tool, and
the type hints define the arguments. So: clear docstrings + type hints = better agent.
"""
# Round 1
from .uniprot import get_uniprot_dossier
from .opentargets import get_target_disease_evidence, get_gene_phenome
from .chembl import get_chembl_modulators
from .mr import get_mr_result, get_mr_outcomes, get_instrument_provenance
# Round 2
from .clinvar import get_clinvar_variants
from .gnomad import get_gnomad_constraint
from .gwas import get_gwas_catalog, get_gwas_associations
from .pharmgkb import get_pharmgkb_drug_gene
# Round 3 - literature and instrument availability
from .litcheck import get_published_mr
from .eqtl import get_eqtl_instruments, instrument_availability
from .gtex import get_gtex_eqtl, tissue_ids, scan_tissue_panel, list_panels

ROUND1_TOOLS = [
    get_uniprot_dossier,
    get_target_disease_evidence,
    get_chembl_modulators,
    get_mr_result,
]

# Tools handed to the agent for a single card. All eight hit live public APIs.
TOOLS = ROUND1_TOOLS + [
    get_clinvar_variants,
    get_gnomad_constraint,
    get_gwas_catalog,
    get_pharmgkb_drug_gene,
]

# Deliberately NOT in TOOLS. `get_published_mr` searches three literature sources and
# judges up to 25 abstracts with a model — tens of seconds and a stack of model calls per
# invocation. Putting it in the card loop would make every card slow and expensive for a
# question most cards don't ask. It is a library entry point for the proteome sweep and
# the evidence-gap work, called explicitly where it is worth the cost.
# `get_gtex_eqtl` is kept out for a different reason: it costs two round trips (symbol ->
# GENCODE id, then a paged association query) and its answer is only meaningful once you
# have decided which TISSUE you mean. That decision belongs to the caller, not to a model
# guessing mid-card.
LIBRARY_ONLY = [
    get_published_mr,
    get_instrument_provenance,
    get_eqtl_instruments,
    instrument_availability,
    get_gtex_eqtl,
    scan_tissue_panel,
    list_panels,
    tissue_ids,
    get_mr_outcomes,
    get_gene_phenome,
    get_gwas_associations,
]
