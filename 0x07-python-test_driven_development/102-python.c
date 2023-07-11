#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_string - This prints string information
 * @q: The Python Object
 * Return: no return
 */
void print_python_string(PyObject *q)
{

	PyObject *str, *repr;

	(void)repr;
	printf("[.] string object info\n");

	if (strcmp(q->ob_type->tp_name, "str"))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(q))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	repr = PyObject_Repr(q);
	str = PyUnicode_AsEncodedString(q, "utf-8", "~E~");
	printf("  length: %ld\n", PyUnicode_GET_SIZE(q));
	printf("  value: %s\n", PyBytes_AsString(str));
}
