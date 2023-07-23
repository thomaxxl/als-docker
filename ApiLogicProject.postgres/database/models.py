# coding: utf-8
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, LargeBinary, SmallInteger, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  July 23, 2023 08:23:34
# Database: postgresql://postgres:p@localhost/postgres
# Dialect:  postgresql
#
# mypy: ignore-errors
########################################################################################################################

from safrs import SAFRSBase
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.postgresql import *



class Category(SAFRSBase, Base):
    __tablename__ = 'categories'
    _s_collection_name = 'Category'  # type: ignore
    __bind_key__ = 'None'

    category_id = Column(SmallInteger, primary_key=True)
    category_name = Column(String(15), nullable=False)
    description = Column(Text)
    picture = Column(LargeBinary)
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)
    ProductList : Mapped[List["Product"]] = relationship(back_populates="category")

    #@jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return ""
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    #@_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = ""

    S_CheckSum = _check_sum_


class CustomerDemographic(SAFRSBase, Base):
    __tablename__ = 'customer_demographics'
    _s_collection_name = 'CustomerDemographic'  # type: ignore
    __bind_key__ = 'None'

    customer_type_id = Column(String(5), primary_key=True)
    customer_desc = Column(Text)
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)
    CustomerCustomerDemoList : Mapped[List["CustomerCustomerDemo"]] = relationship(back_populates="customer_type")

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class Customer(SAFRSBase, Base):
    __tablename__ = 'customers'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    customer_id = Column(String(5), primary_key=True)
    company_name = Column(String(40), nullable=False)
    contact_name = Column(String(30))
    contact_title = Column(String(30))
    address = Column(String(60))
    city = Column(String(15))
    region = Column(String(15))
    postal_code = Column(String(10))
    country = Column(String(15))
    phone = Column(String(24))
    fax = Column(String(24))
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)
    CustomerCustomerDemoList : Mapped[List["CustomerCustomerDemo"]] = relationship(back_populates="customer")
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class Employee(SAFRSBase, Base):
    __tablename__ = 'employees'
    _s_collection_name = 'Employee'  # type: ignore
    __bind_key__ = 'None'

    employee_id = Column(SmallInteger, primary_key=True)
    last_name = Column(String(20), nullable=False)
    first_name = Column(String(10), nullable=False)
    title = Column(String(30))
    title_of_courtesy = Column(String(25))
    birth_date = Column(Date)
    hire_date = Column(Date)
    address = Column(String(60))
    city = Column(String(15))
    region = Column(String(15))
    postal_code = Column(String(10))
    country = Column(String(15))
    home_phone = Column(String(24))
    extension = Column(String(4))
    photo = Column(LargeBinary)
    notes = Column(Text)
    reports_to = Column(ForeignKey('employees.employee_id'))
    photo_path = Column(String(255))
    allow_client_generated_ids = True

    # parent relationships (access parent)
    Employee : Mapped["Employee"] = relationship(remote_side=[employee_id], back_populates=("EmployeeList"))

    # child relationships (access children)
    EmployeeList : Mapped[List["Employee"]] = relationship(back_populates="Employee")
    OrderList : Mapped[List["Order"]] = relationship(back_populates="employee")
    EmployeeTerritoryList : Mapped[List["EmployeeTerritory"]] = relationship(back_populates="employee")

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class Region(SAFRSBase, Base):
    __tablename__ = 'region'
    _s_collection_name = 'Region'  # type: ignore
    __bind_key__ = 'None'

    region_id = Column(SmallInteger, primary_key=True)
    region_description = Column(String(60), nullable=False)
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)
    TerritoryList : Mapped[List["Territory"]] = relationship(back_populates="region")

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class Shipper(SAFRSBase, Base):
    __tablename__ = 'shippers'
    _s_collection_name = 'Shipper'  # type: ignore
    __bind_key__ = 'None'

    shipper_id = Column(SmallInteger, primary_key=True)
    company_name = Column(String(40), nullable=False)
    phone = Column(String(24))
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="shipper")

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class Supplier(SAFRSBase, Base):
    __tablename__ = 'suppliers'
    _s_collection_name = 'Supplier'  # type: ignore
    __bind_key__ = 'None'

    supplier_id = Column(SmallInteger, primary_key=True)
    company_name = Column(String(40), nullable=False)
    contact_name = Column(String(30))
    contact_title = Column(String(30))
    address = Column(String(60))
    city = Column(String(15))
    region = Column(String(15))
    postal_code = Column(String(10))
    country = Column(String(15))
    phone = Column(String(24))
    fax = Column(String(24))
    homepage = Column(Text)
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)
    ProductList : Mapped[List["Product"]] = relationship(back_populates="supplier")

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class UsState(SAFRSBase, Base):
    __tablename__ = 'us_states'
    _s_collection_name = 'UsState'  # type: ignore
    __bind_key__ = 'None'

    state_id = Column(SmallInteger, primary_key=True)
    state_name = Column(String(100))
    state_abbr = Column(String(2))
    state_region = Column(String(50))
    allow_client_generated_ids = True

    # parent relationships (access parent)

    # child relationships (access children)

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class CustomerCustomerDemo(SAFRSBase, Base):
    __tablename__ = 'customer_customer_demo'
    _s_collection_name = 'CustomerCustomerDemo'  # type: ignore
    __bind_key__ = 'None'

    customer_id = Column(ForeignKey('customers.customer_id'), primary_key=True, nullable=False)
    customer_type_id = Column(ForeignKey('customer_demographics.customer_type_id'), primary_key=True, nullable=False)
    allow_client_generated_ids = True

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("CustomerCustomerDemoList"))
    customer_type : Mapped["CustomerDemographic"] = relationship(back_populates=("CustomerCustomerDemoList"))

    # child relationships (access children)

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class Order(SAFRSBase, Base):
    __tablename__ = 'orders'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    order_id = Column(SmallInteger, primary_key=True)
    customer_id = Column(ForeignKey('customers.customer_id'))
    employee_id = Column(ForeignKey('employees.employee_id'))
    order_date = Column(Date)
    required_date = Column(Date)
    shipped_date = Column(Date)
    ship_via = Column(ForeignKey('shippers.shipper_id'))
    freight = Column(Float)
    ship_name = Column(String(40))
    ship_address = Column(String(60))
    ship_city = Column(String(15))
    ship_region = Column(String(15))
    ship_postal_code = Column(String(10))
    ship_country = Column(String(15))
    allow_client_generated_ids = True

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))
    employee : Mapped["Employee"] = relationship(back_populates=("OrderList"))
    shipper : Mapped["Shipper"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)
    OrderDetailList : Mapped[List["OrderDetail"]] = relationship(back_populates="order")

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class Product(SAFRSBase, Base):
    __tablename__ = 'products'
    _s_collection_name = 'Product'  # type: ignore
    __bind_key__ = 'None'

    product_id = Column(SmallInteger, primary_key=True)
    product_name = Column(String(40), nullable=False)
    supplier_id = Column(ForeignKey('suppliers.supplier_id'))
    category_id = Column(ForeignKey('categories.category_id'))
    quantity_per_unit = Column(String(20))
    unit_price = Column(Float)
    units_in_stock = Column(SmallInteger)
    units_on_order = Column(SmallInteger)
    reorder_level = Column(SmallInteger)
    discontinued = Column(Integer, nullable=False)
    allow_client_generated_ids = True

    # parent relationships (access parent)
    category : Mapped["Category"] = relationship(back_populates=("ProductList"))
    supplier : Mapped["Supplier"] = relationship(back_populates=("ProductList"))

    # child relationships (access children)
    OrderDetailList : Mapped[List["OrderDetail"]] = relationship(back_populates="product")

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class Territory(SAFRSBase, Base):
    __tablename__ = 'territories'
    _s_collection_name = 'Territory'  # type: ignore
    __bind_key__ = 'None'

    territory_id = Column(String(20), primary_key=True)
    territory_description = Column(String(60), nullable=False)
    region_id = Column(ForeignKey('region.region_id'), nullable=False)
    allow_client_generated_ids = True

    # parent relationships (access parent)
    region : Mapped["Region"] = relationship(back_populates=("TerritoryList"))

    # child relationships (access children)
    EmployeeTerritoryList : Mapped[List["EmployeeTerritory"]] = relationship(back_populates="territory")

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class EmployeeTerritory(SAFRSBase, Base):
    __tablename__ = 'employee_territories'
    _s_collection_name = 'EmployeeTerritory'  # type: ignore
    __bind_key__ = 'None'

    employee_id = Column(ForeignKey('employees.employee_id'), primary_key=True, nullable=False)
    territory_id = Column(ForeignKey('territories.territory_id'), primary_key=True, nullable=False)
    allow_client_generated_ids = True

    # parent relationships (access parent)
    employee : Mapped["Employee"] = relationship(back_populates=("EmployeeTerritoryList"))
    territory : Mapped["Territory"] = relationship(back_populates=("EmployeeTerritoryList"))

    # child relationships (access children)

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_


class OrderDetail(SAFRSBase, Base):
    __tablename__ = 'order_details'
    _s_collection_name = 'OrderDetail'  # type: ignore
    __bind_key__ = 'None'

    order_id = Column(ForeignKey('orders.order_id'), primary_key=True, nullable=False)
    product_id = Column(ForeignKey('products.product_id'), primary_key=True, nullable=False)
    unit_price = Column(Float, nullable=False)
    quantity = Column(SmallInteger, nullable=False)
    discount = Column(Float, nullable=False)
    allow_client_generated_ids = True

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("OrderDetailList"))
    product : Mapped["Product"] = relationship(back_populates=("OrderDetailList"))

    # child relationships (access children)

    @jsonapi_attr
    def _check_sum_(self):  # type: ignore [no-redef]
        return None if isinstance(self, flask_sqlalchemy.model.DefaultMeta) \
            else self._check_sum_property if hasattr(self,"_check_sum_property") \
                else None  # property does not exist during initialization

    @_check_sum_.setter
    def _check_sum_(self, value):  # type: ignore [no-redef]
        self._check_sum_property = value

    S_CheckSum = _check_sum_
