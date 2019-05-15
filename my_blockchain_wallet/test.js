const secureRandom = require("secure-random");
const elliptic = require('elliptic');
const ecdsa = new elliptic.ec('secp256k1');
const sha256 = require('js-sha256');
const ripemd160 = require('ripemd160');


const max = Buffer.from("0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364140", 'hex');  
let isInvalid = true;  
let privateKey;  
while (isInvalid) {    
  privateKey = secureRandom.randomBuffer(32);
  if (Buffer.compare(max, privateKey) == 1) {      
    isInvalid = false;     
  }  
}
console.log('> Private key: ', privateKey.toString('hex'));