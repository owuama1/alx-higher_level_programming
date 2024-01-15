#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Print information about a Python string object
 * @p: PyObject representing a Python string
 */
void print_python_string(PyObject *p)
{
	if (PyUnicode_Check(p))
	{
		Py_UNICODE *str = PyUnicode_AsUnicode(p);
		Py_ssize_t length = PyUnicode_GetLength(p);

		printf("String data: %ls\n", str);
		printf("Length: %zd\n", length);
	}
	else
	{
		fprintf(stderr, "Invalid Python string\n");
	}
}

/**
 * main - Example usage of the print_python_string function
 * Return: Always 0
 */
int main(void)
{
	/* Initialize the Python interpreter */
	Py_Initialize();

	/* Create a Python string */
	PyObject *pyString = PyUnicode_DecodeUTF8("Hello, Python!", strlen("Hello, Python!"), "strict");

	/* Print the Python string */
	print_python_string(pyString);

	/* Cleanup */
	Py_DECREF(pyString);
	Py_Finalize();

	return (0);
}
