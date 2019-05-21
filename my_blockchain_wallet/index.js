const secureRandom = require("secure-random");
const elliptic = require('elliptic');
const ecdsa = new elliptic.ec('secp256k1');
const sha256 = require('js-sha256');
const ripemd160 = require('ripemd160');
const base58 = require('bs58');
const max = Buffer.from("fffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364140");

var foundPrivateKey = false;
var privateKey;

while (!foundPrivateKey){

    privateKey = secureRandom.randomBuffer(32);
    if (Buffer.compare(max, privateKey) == 1){  
        foundPrivateKey = true;
        console.log("running")
    }
}



console.log("PRIVATE: " + privateKey.toString("hex"));

var keys = ecdsa.keyFromPrivate(privateKey);
var publicKey = keys.getPublic("hex");

console.log("PUBLIC: " + publicKey);

const hashBeforePKH = sha256(Buffer.from(publicKey, 'hex'));
const publicKeyHash = new ripemd160().update(Buffer.from(hashBeforePKH, 'hex')).digest();

console.log("PUBLIC KEY HASH: " + publicKeyHash.toString("hex"));

function createPublicAddress(publicKeyHash) {
    // step 1 - add prefix "00" in hex
    const step1 = Buffer.from("00" + publicKeyHash, 'hex');
    // step 2 - create SHA256 hash of step 1
    const step2 = sha256(step1);
    // step 3 - create SHA256 hash of step 2
    const step3 = sha256(Buffer.from(step2, 'hex'));
    // step 4 - find the 1st byte of step 3 - save as "checksum"
    const checksum = step3.substring(0, 8);
    // step 5 - add step 1 + checksum
    const step4 = step1.toString('hex') + checksum;
    // return base 58 encoding of step 5
    const address = base58.encode(Buffer.from(step4, 'hex'));
    return address;
  }

var tmp = createPublicAddress(publicKeyHash.toString("hex"));

  console.log("A PUBLIC ADRESS KEY HASH: " + tmp.toString("hex"));

  function createPrivateKeyWIF(privateKey) {
    const step1 = Buffer.from("80" + privateKey, 'hex');
    const step2 = sha256(step1);
    const step3 = sha256(Buffer.from(step2, 'hex'));
    const checksum = step3.substring(0, 8);
    const step4 = step1.toString('hex') + checksum;
    const privateKeyWIF = base58.encode(Buffer.from(step4, 'hex'));
    return privateKeyWIF;
  }

  tmp = createPrivateKeyWIF(privateKey.toString("hex"));

  console.log("PRIVATE KEY WIF " + tmp.toString("hex"));