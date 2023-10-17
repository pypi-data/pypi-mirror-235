#ifndef _PYGMLIB_CIPHER_HPP
#define _PYGMLIB_CIPHER_HPP

#include <gmlib/crypto/cipher/CipherMode.hpp>
#include <gmlib/crypto/cipher/Sm4Cipher.h>
#include <gmlib/crypto/cipher/AesCipher.h>
#include <pybind11/pybind11.h>
#include <stdexcept>
#include <memory>

using namespace gmlib;
using namespace std;
namespace py = pybind11;

template <class Cryptor, size_t ObjId = 0>
class CryptoWithoutIV
{
public:
    static constexpr size_t BLOCK_SIZE   = Cryptor::BLOCK_SIZE;
    static constexpr size_t USER_KEY_LEN = Cryptor::USER_KEY_LEN;

private:
    using buf_t = unique_ptr<uint8_t[]>;

private:
    Cryptor crypto;

public:
    CryptoWithoutIV(const py::bytes& key)
    {
        // load key data
        string key_buf = string(key);
        if (key_buf.size() != Cryptor::USER_KEY_LEN)
        {
            throw runtime_error("[pygmlib error]: invalid key length");
        }
        // init crypto
        this->crypto.init((const uint8_t*)(key_buf.c_str()));
    }
    CryptoWithoutIV(const CryptoWithoutIV& other) = default;
    ~CryptoWithoutIV()                            = default;

public:
    py::bytes update(const py::bytes& in)
    {
        string in_buf(in);
        size_t max_outl = in_buf.size() + Cryptor::BLOCK_SIZE;
        size_t outl;
        buf_t  out_buf(new uint8_t[max_outl]);
        this->crypto.update(out_buf.get(), &outl,
                            (const uint8_t*)(in_buf.c_str()), in_buf.size());
        return py::bytes((const char*)(out_buf.get()), outl);
    }

    py::bytes final()
    {
        size_t outl;
        buf_t  out_buf(new uint8_t[Cryptor::BLOCK_SIZE]);
        this->crypto.final(out_buf.get(), &outl);
        return py::bytes((const char*)(out_buf.get()), outl);
    }
};

template <class Cryptor, size_t ObjId = 0>
class CryptoWithIV
{
public:
    static constexpr size_t BLOCK_SIZE   = Cryptor::BLOCK_SIZE;
    static constexpr size_t USER_KEY_LEN = Cryptor::USER_KEY_LEN;

private:
    using buf_t = unique_ptr<uint8_t[]>;

private:
    Cryptor crypto;

public:
    CryptoWithIV(const py::bytes& key, const py::bytes& iv)
    {
        // load key data
        string key_buf = string(key);
        string iv_buf  = string(iv);
        if (key_buf.size() != Cryptor::USER_KEY_LEN)
        {
            throw runtime_error("[pygmlib error]: invalid key length");
        }
        if (iv_buf.size() != Cryptor::BLOCK_SIZE)
        {
            throw runtime_error("[pygmlib error]: invalid iv length");
        }
        // init crypto
        this->crypto.init((const uint8_t*)(key_buf.c_str()),
                          (const uint8_t*)(iv_buf.c_str()));
    }
    CryptoWithIV(const CryptoWithIV& other) = default;
    ~CryptoWithIV()                         = default;

public:
    py::bytes update(const py::bytes& in)
    {
        string in_buf(in);
        size_t max_outl = in_buf.size() + Cryptor::BLOCK_SIZE;
        size_t outl;
        buf_t  out_buf(new uint8_t[max_outl]);
        this->crypto.update(out_buf.get(), &outl,
                            (const uint8_t*)(in_buf.c_str()), in_buf.size());
        return py::bytes((const char*)(out_buf.get()), outl);
    }

    py::bytes final()
    {
        size_t outl;
        buf_t  out_buf(new uint8_t[Cryptor::BLOCK_SIZE]);
        this->crypto.final(out_buf.get(), &outl);
        return py::bytes((const char*)(out_buf.get()), outl);
    }
};

template <class Cryptor, size_t ObjId = 0>
class CryptoGcmEnc
{
public:
    static constexpr size_t BLOCK_SIZE   = Cryptor::BLOCK_SIZE;
    static constexpr size_t USER_KEY_LEN = Cryptor::USER_KEY_LEN;

private:
    using buf_t = unique_ptr<uint8_t[]>;

private:
    Cryptor crypto;

public:
    CryptoGcmEnc(const py::bytes& key,
                 const py::bytes& iv,
                 const py::bytes& aad)
    {
        // load key data
        string key_buf = string(key);
        string iv_buf  = string(iv);
        string aad_buf = string(aad);
        if (key_buf.size() != Cryptor::USER_KEY_LEN)
        {
            throw runtime_error("[pygmlib error]: invalid key length");
        }
        // init crypto
        this->crypto.init((const uint8_t*)(key_buf.c_str()),
                          (const uint8_t*)(iv_buf.c_str()), iv_buf.size(),
                          (const uint8_t*)(aad_buf.c_str()), aad_buf.size());
    }
    CryptoGcmEnc(const CryptoGcmEnc& other) = default;
    ~CryptoGcmEnc()                         = default;

public:
    py::bytes get_tag()
    {
        uint8_t tag[16];
        this->crypto.get_tag(tag);
        return py::bytes((const char*)tag, 16);
    }

public:
    py::bytes update(const py::bytes& in)
    {
        string in_buf(in);
        size_t max_outl = in_buf.size() + Cryptor::BLOCK_SIZE;
        size_t outl;
        buf_t  out_buf(new uint8_t[max_outl]);
        this->crypto.update(out_buf.get(), &outl,
                            (const uint8_t*)(in_buf.c_str()), in_buf.size());
        return py::bytes((const char*)(out_buf.get()), outl);
    }

    py::bytes final()
    {
        size_t outl;
        buf_t  out_buf(new uint8_t[Cryptor::BLOCK_SIZE]);
        this->crypto.final(out_buf.get(), &outl);
        return py::bytes((const char*)(out_buf.get()), outl);
    }
};

template <class Cryptor, size_t ObjId = 0>
class CryptoGcmDec
{
public:
    static constexpr size_t BLOCK_SIZE   = Cryptor::BLOCK_SIZE;
    static constexpr size_t USER_KEY_LEN = Cryptor::USER_KEY_LEN;

private:
    using buf_t = unique_ptr<uint8_t[]>;

private:
    Cryptor crypto;

public:
    CryptoGcmDec(const py::bytes& key,
                 const py::bytes& iv,
                 const py::bytes& aad)
    {
        // load key data
        string key_buf = string(key);
        string iv_buf  = string(iv);
        string aad_buf = string(aad);
        if (key_buf.size() != Cryptor::USER_KEY_LEN)
        {
            throw runtime_error("[pygmlib error]: invalid key length");
        }
        // init crypto
        this->crypto.init((const uint8_t*)(key_buf.c_str()),
                          (const uint8_t*)(iv_buf.c_str()), iv_buf.size(),
                          (const uint8_t*)(aad_buf.c_str()), aad_buf.size());
    }
    CryptoGcmDec(const CryptoGcmDec& other) = default;
    ~CryptoGcmDec()                         = default;

public:
    void set_tag(const py::bytes& tag)
    {
        string tag_buf(tag);
        if (tag_buf.size() != 16)
        {
            throw runtime_error("invalid gcm tag length, need 16");
        }
        this->crypto.set_tag((const uint8_t*)(tag_buf.c_str()));
    }

public:
    py::bytes update(const py::bytes& in)
    {
        string in_buf(in);
        size_t max_outl = in_buf.size() + Cryptor::BLOCK_SIZE;
        size_t outl;
        buf_t  out_buf(new uint8_t[max_outl]);
        this->crypto.update(out_buf.get(), &outl,
                            (const uint8_t*)(in_buf.c_str()), in_buf.size());
        return py::bytes((const char*)(out_buf.get()), outl);
    }

    py::bytes final()
    {
        size_t outl;
        buf_t  out_buf(new uint8_t[Cryptor::BLOCK_SIZE]);
        this->crypto.final(out_buf.get(), &outl);
        return py::bytes((const char*)(out_buf.get()), outl);
    }
};

static const char* DOC_CryptoWithoutIV_init = R"(
    Parameters
    ----------
    :param key: User Key
)";

static const char* DOC_CryptoWithIV_init = R"(
    Parameters
    ----------
    :param key: User Key
    :param iv:  Unique initialisation vector
)";

static const char* DOC_CryptoGcm_init = R"(
    Parameters
    ----------
    :param key: User Key
    :param iv:  Unique initialisation vector
    :param aad: Additional Authenticated Data
)";

#define _PYMODULE_ADD_CryptoWithoutIV(m, name)                    \
    py::class_<name>(m, #name)                                    \
        .def(py::init<const py::bytes&>(), py::arg("key"),        \
             DOC_CryptoWithoutIV_init)                            \
        .def_readonly_static("USER_KEY_LEN", &name::USER_KEY_LEN) \
        .def_readonly_static("BLOCK_SIZE", &name::BLOCK_SIZE)     \
        .def("update", &name::update, py::arg("data"))            \
        .def("final", &name::final)

#define _PYMODULE_ADD_CryptoWithIV(m, name)                                  \
    py::class_<name>(m, #name)                                               \
        .def(py::init<const py::bytes&, const py::bytes&>(), py::arg("key"), \
             py::arg("iv"), DOC_CryptoWithIV_init)                           \
        .def_readonly_static("USER_KEY_LEN", &name::USER_KEY_LEN)            \
        .def_readonly_static("BLOCK_SIZE", &name::BLOCK_SIZE)                \
        .def("update", &name::update, py::arg("data"))                       \
        .def("final", &name::final)

#define _PYMODULE_ADD_CryptoGcmEnc(m, name)                                    \
    py::class_<name>(m, #name)                                                 \
        .def(py::init<const py::bytes&, const py::bytes&, const py::bytes&>(), \
             py::arg("key"), py::arg("iv"), py::arg("aad"),                    \
             DOC_CryptoGcm_init)                                               \
        .def_readonly_static("USER_KEY_LEN", &name::USER_KEY_LEN)              \
        .def_readonly_static("BLOCK_SIZE", &name::BLOCK_SIZE)                  \
        .def("update", &name::update, py::arg("data"))                         \
        .def("final", &name::final)                                            \
        .def("get_tag", &name::get_tag)

#define _PYMODULE_ADD_CryptoGcmDec(m, name)                                    \
    py::class_<name>(m, #name)                                                 \
        .def(py::init<const py::bytes&, const py::bytes&, const py::bytes&>(), \
             py::arg("key"), py::arg("iv"), py::arg("aad"),                    \
             DOC_CryptoGcm_init)                                               \
        .def_readonly_static("USER_KEY_LEN", &name::USER_KEY_LEN)              \
        .def_readonly_static("BLOCK_SIZE", &name::BLOCK_SIZE)                  \
        .def("update", &name::update, py::arg("data"))                         \
        .def("final", &name::final)                                            \
        .def("set_tag", &name::set_tag, py::arg("tag"))

#define CryptoEcbEncryptor(cipher) CryptoWithoutIV<EcbEncryptor<cipher>, 0>
#define CryptoEcbDecryptor(cipher) CryptoWithoutIV<EcbDecryptor<cipher>, 1>
#define CryptoCbcEncryptor(cipher) CryptoWithIV<CbcEncryptor<cipher>, 0>
#define CryptoCbcDecryptor(cipher) CryptoWithIV<CbcDecryptor<cipher>, 1>
#define CryptoCfbEncryptor(cipher) CryptoWithIV<CfbEncryptor<cipher>, 0>
#define CryptoCfbDecryptor(cipher) CryptoWithIV<CfbDecryptor<cipher>, 1>
#define CryptoOfbEncryptor(cipher) CryptoWithIV<OfbEncryptor<cipher>, 0>
#define CryptoOfbDecryptor(cipher) CryptoWithIV<OfbDecryptor<cipher>, 1>
#define CryptoCtrEncryptor(cipher) CryptoWithIV<CtrEncryptor<cipher>, 0>
#define CryptoCtrDecryptor(cipher) CryptoWithIV<CtrDecryptor<cipher>, 1>
#define CryptoGcmEncryptor(cipher) CryptoGcmEnc<GcmEncryptor<cipher>, 0>
#define CryptoGcmDecryptor(cipher) CryptoGcmDec<GcmDecryptor<cipher>, 1>

#define PYMODULE_ADD_ECB(m, name)     _PYMODULE_ADD_CryptoWithoutIV(m, name)
#define PYMODULE_ADD_CBC(m, name)     _PYMODULE_ADD_CryptoWithIV(m, name)
#define PYMODULE_ADD_CFB(m, name)     _PYMODULE_ADD_CryptoWithIV(m, name)
#define PYMODULE_ADD_OFB(m, name)     _PYMODULE_ADD_CryptoWithIV(m, name)
#define PYMODULE_ADD_CTR(m, name)     _PYMODULE_ADD_CryptoWithIV(m, name)
#define PYMODULE_ADD_GCM_ENC(m, name) _PYMODULE_ADD_CryptoGcmEnc(m, name)
#define PYMODULE_ADD_GCM_DEC(m, name) _PYMODULE_ADD_CryptoGcmDec(m, name)

#endif