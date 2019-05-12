const secureRandom = require("secure-random");
const elliptic = require('elliptic');
const ecdsa = new elliptic.ec('secp256k1');
const sha256 = require('js-sha256');
const ripemd160 = require('ripemd160');
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

console.log("FINAL, PUBLIC KEY HASH: " + publicKeyHash.toString("hex"));