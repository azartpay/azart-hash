#include <Python.h>

#include "azart.h"

static PyObject *azart_getpowhash(PyObject *self, PyObject *args)
{
    char *output;
    PyObject *value;
#if PY_MAJOR_VERSION >= 3
    PyBytesObject *input;
#else
    PyStringObject *input;
#endif
    if (!PyArg_ParseTuple(args, "S", &input))
        return NULL;
    Py_INCREF(input);
    output = PyMem_Malloc(32);

#if PY_MAJOR_VERSION >= 3
    azart_hash((char *)PyBytes_AsString((PyObject*) input), (int)PyBytes_Size((PyObject*) input), output);
#else
    azart_hash((char *)PyString_AsString((PyObject*) input), (int)PyString_Size((PyObject*) input), output);
#endif
    Py_DECREF(input);
#if PY_MAJOR_VERSION >= 3
    value = Py_BuildValue("y#", output, 32);
#else
    value = Py_BuildValue("s#", output, 32);
#endif
    PyMem_Free(output);
    return value;
}

static PyMethodDef AzartMethods[] = {
    { "getPoWHash", azart_getpowhash, METH_VARARGS, "Returns the proof of work hash using azart hash" },
    { NULL, NULL, 0, NULL }
};

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef AzartModule = {
    PyModuleDef_HEAD_INIT,
    "azart_hash",
    "...",
    -1,
    AzartMethods
};

PyMODINIT_FUNC PyInit_azart_hash(void) {
    return PyModule_Create(&AzartModule);
}

#else

PyMODINIT_FUNC initazart_hash(void) {
    (void) Py_InitModule("azart_hash", AzartMethods);
}
#endif
