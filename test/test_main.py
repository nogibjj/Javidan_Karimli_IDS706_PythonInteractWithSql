from src.main import perform_elt, crud_operations, perform_analytics


def test_main():
    res = perform_elt()
    res2 = crud_operations()
    res3 = perform_analytics()

    assert res
    assert res2
    assert res3
