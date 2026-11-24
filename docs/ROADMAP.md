# Research roadmap

AOMNIYA is an experimental architecture, not demonstrated AGI. The existing README proposes Phi, causal DAG, spectral representation and content-addressed memory. Their usefulness is unproven; in particular the golden ratio is a candidate parameter, not an established stability principle.

Current implementation: a minimal spectral transform and input digest in src/agent.py. It does not implement the full four-part architecture.

Next: implement DAG validation and content-addressed memory; compare Phi sizing against uniform and geometric alternatives under matched budgets; compare spectral and raw representations on held-out tasks. Record negative results. Avoid claims of general intelligence without independent evaluation.

Run smoke checks: python -m unittest discover -s tests
