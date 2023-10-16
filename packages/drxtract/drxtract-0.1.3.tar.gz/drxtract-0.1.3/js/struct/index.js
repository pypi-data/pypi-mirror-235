// Author: Abraham Macias Paredes
// E-mail: system252001@yahoo.es
// License: GNU GPL v2 (see LICENSE file for details).

//
// Python struct package replacement
//

function toSigned(value, len) {
  var umax = 0xFF;
  var imax = 0x7F;
  for (var i = 1; i<len; i++) {
    umax = (umax<<8) + 0xFF;
    imax = (imax<<8) + 0xFF;
  }
  
  if (value > imax) {
    value -= umax;
  }
  
  return [value, len];
}

function unpackChar(data, idx) {
  return [data[idx], 1];
}

function unpackSignedChar(data, idx) {
  const [value, len] = unpackChar(data, idx);
  return toSigned(value, len);
}

const leUnpackOperations = {};
leUnpackOperations['c'] = unpackChar;
leUnpackOperations['b'] = unpackSignedChar;
leUnpackOperations['B'] = unpackChar;

leUnpackOperations['h'] = function(data, idx) {
  const [value, len] = leUnpackOperations['H'](data, idx);
  return toSigned(value, len);
}

leUnpackOperations['H'] = function(data, idx) {
  return [data[idx] + (data[idx+1]<<8), 2];
}

leUnpackOperations['i'] = function(data, idx) {
  const [value, len] = leUnpackOperations['I'](data, idx);
  return toSigned(value, len);
}

leUnpackOperations['I'] = function(data, idx) {
  return [data[idx] + (data[idx+1]<<8) + (data[idx+2]<<16)
          + (data[idx+3]<<24), 4];
}

const beUnpackOperations = {};
beUnpackOperations['c'] = unpackChar;
beUnpackOperations['b'] = unpackSignedChar;
beUnpackOperations['B'] = unpackChar;

beUnpackOperations['h'] = function(data, idx) {
  const [value, len] = beUnpackOperations['H'](data, idx);
  return toSigned(value, len);
}

beUnpackOperations['H'] = function(data, idx) {
  return [(data[idx]<<8) + data[idx+1], 2];
}

beUnpackOperations['i'] = function(data, idx) {
  const [value, len] = beUnpackOperations['I'](data, idx);
  return toSigned(value, len);
}

beUnpackOperations['I'] = function(data, idx) {
  return [(data[idx]<<24) + (data[idx+1]<<16) + (data[idx+2]<<8)
          + data[idx+3], 4];
}

const unpackOperations = {};
unpackOperations['<'] = leUnpackOperations;
unpackOperations['>'] = beUnpackOperations;
unpackOperations['!'] = beUnpackOperations;


exports.unpack = (format, data) => {
  const endian = format[0];
  const unpacked = [];
  const operations = unpackOperations[endian];
  if (operations) {
    var i = 1;
    var idx = 0;
    
    while (i < format.length) {
      const f = format[i];
      const op = operations[f];
      if (!op) {
        throw new Error("Format not detected: " + f);
      }
      const [value, len] = op(data, idx);
      idx += len;
      i++;
      unpacked.push(value);
    }
    
  } else {
    throw new Error("Endian not detected: " + endian);
  }
  return unpacked;
}

