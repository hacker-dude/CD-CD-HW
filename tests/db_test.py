import pytest
from resources.fixtures import db_cursor
from resources.fixtures import db_connection
import allure


@allure.story("AW2012 DQ")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.database_DQ
def test_first_and_last_name_not_null(db_cursor):
    """
    Verify that the Person.Person table does not contain NULL values
    in the FirstName or LastName columns.
    """
    with allure.step("Execute Query"):
        SQL_QUERY = """
        SELECT BusinessEntityID, FirstName, LastName
        FROM Person.Person
        WHERE FirstName IS NULL OR LastName IS NULL;
        """
    db_cursor.execute(SQL_QUERY)
    records = db_cursor.fetchall()
    with allure.step("Assert results"):
        assert len(records) == 0, (
            f"Found {len(records)} records with missing first or last name."
        )


@allure.story("AW2012 DQ")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.database_DQ
def test_email_format(db_cursor):
    """
    Ensure all email addresses in Person.EmailAddress follow a valid format.
    """
    with allure.step("Execute Query"):
        SQL_QUERY = """
        SELECT EmailAddress
        FROM Person.EmailAddress
        WHERE EmailAddress NOT LIKE '%_@_%._%';
        """
    db_cursor.execute(SQL_QUERY)
    records = db_cursor.fetchall()
    with allure.step("Assert results"):
        assert len(records) == 0, (
            f"Found {len(records)} records with invalid email format."
        )


@allure.story("AW2012 DQ")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.database_DQ
def test_order_date_not_in_future(db_cursor):
    """
    Validate that no order in Sales.SalesOrderHeader has an OrderDate set in the future.
    """
    with allure.step("Execute Query"):
        SQL_QUERY = """
        SELECT SalesOrderID, OrderDate
        FROM Sales.SalesOrderHeader
        WHERE OrderDate > GETDATE();
        """
    db_cursor.execute(SQL_QUERY)
    records = db_cursor.fetchall()
    with allure.step("Assert results"):
        assert len(records) == 0, f"Found {len(records)} orders with future dates."


@allure.story("AW2012 DQ")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.database_DQ
def test_total_due_positive(db_cursor):
    """
    Ensure that all sales orders have a TotalDue value greater than zero.
    """
    with allure.step("Execute Query"):
        SQL_QUERY = """
        SELECT SalesOrderID, TotalDue
        FROM Sales.SalesOrderHeader
        WHERE TotalDue <= 0;
        """
    db_cursor.execute(SQL_QUERY)
    records = db_cursor.fetchall()
    with allure.step("Assert results"):
        assert len(records) == 0, (
            f"Found {len(records)} orders with zero or negative TotalDue."
        )


@allure.story("AW2012 DQ")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.database_DQ
def test_unique_product_names(db_cursor):
    """
    Check that product names in Production.Product are unique.
    """
    with allure.step("Execute Query"):
        SQL_QUERY = """
        SELECT Name, COUNT(*)
        FROM Production.Product
        GROUP BY Name
        HAVING COUNT(*) > 1;
        """
    db_cursor.execute(SQL_QUERY)
    records = db_cursor.fetchall()
    with allure.step("Assert results"):
        assert len(records) == 0, f"Found {len(records)} duplicate product names."


@allure.story("AW2012 DQ")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.database_DQ
def test_product_price_non_negative(db_cursor):
    """
    Ensure that all products in Production.Product have a non-negative ListPrice.
    """
    with allure.step("Execute Query"):
        SQL_QUERY = """
        SELECT ProductID, Name, ListPrice
        FROM Production.Product
        WHERE ListPrice < 0;
        """
    db_cursor.execute(SQL_QUERY)
    records = db_cursor.fetchall()
    with allure.step("Assert results"):
        assert len(records) == 0, (
            f"Found {len(records)} products with negative ListPrice."
        )
