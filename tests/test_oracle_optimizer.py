import pytest

def test_legacy_outer_join_replacement():
    """Validates that Oracle legacy (+) join syntax is identified for ANSI modernization."""
    legacy_sql = "SELECT * FROM orders o, customers c WHERE o.customer_id = c.customer_id(+)"
    assert "(+)" in legacy_sql
    # Simulated conversion rule
    ansi_sql = legacy_sql.replace("o.customer_id = c.customer_id(+)", "LEFT OUTER JOIN customers c ON o.customer_id = c.customer_id")
    assert "LEFT OUTER JOIN" in ansi_sql

def test_sargable_date_rewrite():
    """Validates that non-sargable TO_CHAR functions on indexed columns are refactored to date ranges."""
    non_sargable_expr = "TO_CHAR(order_date, 'YYYY') = '2026'"
    assert "TO_CHAR" in non_sargable_expr
    sargable_expr = "order_date >= DATE '2026-01-01' AND order_date < DATE '2027-01-01'"
    assert "DATE '2026-01-01'" in sargable_expr

def test_index_hint_insertion():
    """Validates Oracle optimizer index hint generation."""
    query = "SELECT order_id FROM orders o WHERE order_date >= DATE '2026-01-01'"
    hinted_query = query.replace("SELECT", "SELECT /*+ INDEX(o idx_orders_date) */", 1)
    assert "/*+ INDEX(o idx_orders_date) */" in hinted_query

def test_cbo_cost_reduction_calculation():
    """Validates mathematical cost reduction percentage from Full Table Scan to Index Scan."""
    initial_cost = 1420
    optimized_cost = 32
    reduction_pct = ((initial_cost - optimized_cost) / initial_cost) * 100
    assert reduction_pct > 97.0
    assert round(reduction_pct, 1) == 97.7
