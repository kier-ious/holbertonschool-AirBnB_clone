#!/usr/bin/python3
"""unittests for BaseModel"""
import unittest
import pep8
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModelDoc(unittest.TestCase):
    """check BaseModel documentation"""
    def test_class_documentation(self):
        self.assertTrue(len(BaseModel.__doc__) > 0)


class TestBaseModelPycode(unittest.TestCase):
    """check pycodestyle"""
    def test_pycode(self):
        pep8style = pep8.StyleGuide(quiet=True)
        files = [
            'models/base_model.py'
            'tests/test_models/test_base_model.py'
        ]
        result = pep8style.check_files(files)
        self.assertEqual(
            result.total_errors, 0, "PEP 8 style issues found"
        )


class TestBaseModel(unittest.TestCase):
    """tests for BaseModel"""
    def setUp(self):
        """setUp code for tests"""
        pass

    def tearDown(self):
        """cleanup code after tests"""
        pass

    def test_init(self):
        """test base constructor"""
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_save(self):
        """test save method"""
        base_model = BaseModel()
        before_update = base_model.updated_at
        base_model.save()
        self.assertNotEqual(before_update, base_model.updated_at)

    def test_to_dict(self):
        """tests the to_dict method"""
        base_model = BaseModel()
        inst_dict = base_model.to_dict()

        self.assertIn("__class__", inst_dict)
        self.assertIn("created_at", inst_dict)
        self.assertIn("updated_at", inst_dict)
        self.assertIn("id", inst_dict)

        self.assertEqual(inst_dict["__class__"], "BaseModel")
        self.assertEqual(
            inst_dict["created_at"], base_model.created_at.isoformat()
        )
        self.assertEqual(
            inst_dict["updated_at"], base_model.created_at.isoformat()
        )
        self.assertIsInstance(inst_dict["id"], str)

    def test_str(self):
        """test __str__ method"""
        base_model = BaseModel()
        str_rep = str(base_model)
        self.assertIn(f"[BaseModel] ({base_model.id})", str_rep)

    def test_equal(self):
        """test = and !="""
        base_1 = BaseModel()
        base_2 = BaseModel()
        self.assertEqual(base_1, base_1)
        self.assertNotEqual(base_1, base_2)

    def test_empty(self):
        """test empty id"""
        base_1 = BaseModel(id="")
        self.assertEqual(base_1.id, "")

    def test_invalid_input(self):
        """test invalid input"""
        with self.assertRaises(ValueError):
            base_1 = BaseModel(created_at="invalid_datetimte_format")

    def test_serialize(self):
        """test serialization and deserialization"""
        base_1 = BaseModel()
        serialized_data = base_1.to_dict()
        deserialized_base = BaseModel(**serialized_data)
        self.assertEqual(base_1, deserialized_base)


if __name__ == "__main__":
    unittest.main()
