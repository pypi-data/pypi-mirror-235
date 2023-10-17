#include "pygmlib_cipher.hpp"
#include "pygmlib_hash.hpp"
#include <gmlib/crypto/cipher/Sm4Cipher.h>
#include <gmlib/crypto/cipher/AesCipher.h>
#include <gmlib/crypto/hash/Sm3Cipher.h>

#define PYMODULE_ADD_ALL_CRYPTO(m, name)                         \
    using name##EcbEncryptor = CryptoEcbEncryptor(name##Cipher); \
    using name##EcbDecryptor = CryptoEcbDecryptor(name##Cipher); \
    using name##CbcEncryptor = CryptoCbcEncryptor(name##Cipher); \
    using name##CbcDecryptor = CryptoCbcDecryptor(name##Cipher); \
    using name##CfbEncryptor = CryptoCfbEncryptor(name##Cipher); \
    using name##CfbDecryptor = CryptoCfbDecryptor(name##Cipher); \
    using name##OfbEncryptor = CryptoOfbEncryptor(name##Cipher); \
    using name##OfbDecryptor = CryptoOfbDecryptor(name##Cipher); \
    using name##CtrEncryptor = CryptoCtrEncryptor(name##Cipher); \
    using name##CtrDecryptor = CryptoCtrDecryptor(name##Cipher); \
    using name##GcmEncryptor = CryptoGcmEncryptor(name##Cipher); \
    using name##GcmDecryptor = CryptoGcmDecryptor(name##Cipher); \
    PYMODULE_ADD_ECB(m, name##EcbEncryptor);                     \
    PYMODULE_ADD_ECB(m, name##EcbDecryptor);                     \
    PYMODULE_ADD_CBC(m, name##CbcEncryptor);                     \
    PYMODULE_ADD_CBC(m, name##CbcDecryptor);                     \
    PYMODULE_ADD_CFB(m, name##CfbEncryptor);                     \
    PYMODULE_ADD_CFB(m, name##CfbDecryptor);                     \
    PYMODULE_ADD_OFB(m, name##OfbEncryptor);                     \
    PYMODULE_ADD_OFB(m, name##OfbDecryptor);                     \
    PYMODULE_ADD_CTR(m, name##CtrEncryptor);                     \
    PYMODULE_ADD_CTR(m, name##CtrDecryptor);                     \
    PYMODULE_ADD_GCM_ENC(m, name##GcmEncryptor);                 \
    PYMODULE_ADD_GCM_DEC(m, name##GcmDecryptor);

PYBIND11_MODULE(pygmlib, m)
{
    m.doc() = "python bind of GMLib";
    // pygmlib.cipher
    auto m_cipher = m.def_submodule("cipher", "Symmetric Cipher");
    PYMODULE_ADD_ALL_CRYPTO(m_cipher, Sm4);
    PYMODULE_ADD_ALL_CRYPTO(m_cipher, Aes128);
    PYMODULE_ADD_ALL_CRYPTO(m_cipher, Aes192);
    PYMODULE_ADD_ALL_CRYPTO(m_cipher, Aes256);
    // pygmlib.hash
    auto m_hash = m.def_submodule("hash", "Hash Cipher");
    PYMODULE_ADD_HASH(m_hash, Sm3);
}