#include <Python.h>

/**
 * print_python_list - Print information about a Python list
 * @p: PyObject representing a Python list
 */
void print_python_list(PyObject *p) {
    Py_ssize_t i, size;

    size = ((PyVarObject *)p)->ob_size;
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        printf("Element %ld: %s\n", i, Py_TYPE(PyList_GET_ITEM(p, i))->tp_name);
    }
}

/**
 * print_python_bytes - Print information about a Python bytes object
 * @p: PyObject representing a Python bytes object
 */
void print_python_bytes(PyObject *p) {
    Py_ssize_t i, size;
    char *bytes_str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)p)->ob_size;
    bytes_str = ((PyBytesObject *)p)->ob_sval;

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", bytes_str);

    printf("  first 10 bytes: ");
    for (i = 0; i < size && i < 10; i++) {
        printf("%02hhx", bytes_str[i]);
        if (i + 1 < size && i + 1 < 10)
            printf(" ");
    }
	printf("\n");
}
