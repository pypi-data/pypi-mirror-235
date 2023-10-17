#ifndef _PYGMLIB_HASH_HPP
#define _PYGMLIB_HASH_HPP

#include <gmlib/crypto/cipher/CipherMode.hpp>
#include <gmlib/crypto/cipher/Sm4Cipher.h>
#include <gmlib/crypto/cipher/AesCipher.h>
#include <pybind11/pybind11.h>
#include <stdexcept>
#include <memory>

using namespace gmlib;
using namespace std;
namespace py = pybind11;

template <class HashCipher>
class Hash
{
public:
    static constexpr size_t DIGEST_SIZE = HashCipher::DIGEST_SIZE;

private:
    HashCipher hash;

public:
    void update(const py::bytes& in)
    {
        string in_buf(in);
        this->hash.update((const uint8_t*)(in_buf.c_str()), in_buf.size());
    }

    py::bytes final()
    {
        uint8_t digest[HashCipher::DIGEST_SIZE];
        this->hash.final(digest);
        return py::bytes((const char*)digest, HashCipher::DIGEST_SIZE);
    }
};

#define PYMODULE_ADD_HASH(m, name)                                         \
    using _##name##Cipher = Hash<##name##Cipher>;                          \
    py::class_<_##name##Cipher>(m, #name "Cipher")                         \
        .def(py::init<>())                                                 \
        .def_readonly_static("DIGEST_SIZE", &_##name##Cipher::DIGEST_SIZE) \
        .def("update", &_##name##Cipher::update, py::arg("data"))          \
        .def("final", &_##name##Cipher::final)

#endif