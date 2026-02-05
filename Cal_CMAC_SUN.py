from binascii import unhexlify
from Crypto.Cipher import AES
from Crypto.Hash import CMAC

# ==========================================================
# INPUTS (CHANGE THESE)
# ==========================================================
UID_HEX = "BOLT_CARD_UID"
COUNTER = COUNTER_NUMBER

K1_HEX = "YOUR_K1_FROM_BOLT_CARD"  # SDMMetaReadKey
K2_HEX = "YOUR_K2_FROM_BOLT_CARD"  # SDMFileReadKey

DOMAIN = "YOUR_LIGHTNING_NODE_URL"
EXTERNAL_ID = "YOUR_EXTERNAL_ID"

PATH = "/boltcards/api/v1/scan"
# ==========================================================

uid = unhexlify(UID_HEX)
k1 = unhexlify(K1_HEX)
k2 = unhexlify(K2_HEX)

counter_le = COUNTER.to_bytes(3, "little")

# ==========================================================
# STEP 1 — GENERATE SUN (p)
# ==========================================================
picc_plain = (
    b"\x01" +                # PICCDataTag
    uid +
    counter_le +
    b"\x00" * (16 - 1 - len(uid) - len(counter_le))
)

aes = AES.new(k1, AES.MODE_CBC, iv=b"\x00" * 16)
sun = aes.encrypt(picc_plain)

SUN = sun.hex().upper()

# ==========================================================
# STEP 2 — GENERATE CMAC (c) — LNbits logic
# ==========================================================
SV2 = bytes.fromhex("3CC300010080")

# Derive session MAC key
cm1 = CMAC.new(k2, ciphermod=AES)
cm1.update(SV2 + uid + counter_le)
k_ses_mac = cm1.digest()

# CMAC empty message
cm2 = CMAC.new(k_ses_mac, ciphermod=AES)
full_cmac = cm2.digest()

# LNbits truncation (odd bytes)
CMAC = bytes(full_cmac[i] for i in range(1, 16, 2)).hex().upper()

# ==========================================================
# STEP 3 — BUILD LNURLW
# ==========================================================
lnurlw = (
    f"lnurlw:{DOMAIN}"
    f"{PATH}/{EXTERNAL_ID}"
    f"?p={SUN}&c={CMAC}"
)

# ==========================================================
# OUTPUT
# ==========================================================
print("SUN (p):", SUN)
print("CMAC (c):", CMAC)
print()
print("LNURLW:")
print(lnurlw)
