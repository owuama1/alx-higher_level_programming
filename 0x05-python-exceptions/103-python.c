#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Print information about a Python list object
 * @p: PyObject pointer to a Python list
 */
void print_python_list(PyObject *p) {
    Py_ssize_t size, i;

    if (!PyObject_HasAttrString(p, "append")) {
        fprintf(stderr, "Invalid List Object\n");
        return;
    }

    size = ((PyVarObject *)p)->ob_size;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
      printf("Element %ld: %s\n", i, ((PyObject *)(PySequence_ITEM(p, i)))->ob_type->tp_name); 
    }
}

/**
 * print_python_bytes - Print information about a Python bytes object
 * @p: PyObject pointer to a Python bytes object
 */
void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *repr;

    if (!PyObject_HasAttrString(p, "join")) {
        fprintf(stderr, "Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)p)->ob_size;
    repr = PyUnicode_AsUTF8(PyObject_Repr(p));

    printf("[.] bytes object info\n");
    printf("size: %ld\n", size);
    printf("trying string: %s\n", repr);

    printf("first 10 bytes: ");
    for (i = 0; i < size && i < 10; i++) {
        printf("%02hhx", repr[i]);
        if (i + 1 < size && i + 1 < 10)
            printf(" ");
    }
    printf("\n");
}

/**
 * print_python_float - Print information about a Python float object
 * @p: PyObject pointer to a Python float
 */
void print_python_float(PyObject *p) {
    double value;

    if (!PyObject_HasAttrString(p, "real")) {
        fprintf(stderr, "Invalid Float Object\n");
        return;
    }

    value = PyFloat_AsDouble(p);

    printf("[.] float object info\n");
    printf("value: %f\n", value);
}

