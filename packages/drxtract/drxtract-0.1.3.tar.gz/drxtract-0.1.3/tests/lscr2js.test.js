// Author: Abraham Macias Paredes
// E-mail: system252001@yahoo.es
// License: GNU GPL v2 (see LICENSE file for details).

//
// Unit test for lscr2js
//
import {expect} from 'chai';
import * as fs from 'fs';
import * as path from 'path';

import {unpack} from 'struct';
import {parse_lnam_file_data} from '../js/drxtract/lingosrc/parse/lnam.js';
import {parse_lrcr_file_data} from '../js/drxtract/lingosrc/parse/lscr.js';
import {generate_js_code} from '../js/drxtract/lingosrc/codegen/js.js';

import { URL } from 'url';

const __filename = new URL('', import.meta.url).pathname;
const __dirname = new URL('.', import.meta.url).pathname;

describe("struct tests", function () {
    it("Should unpack signed byte", function () {
      const uint8 = new Uint8Array([0x99]);
      const data = unpack('>b', uint8);
      expect(data[0]).to.equal(-102);
    });  
  
    it("Should unpack unsigned byte", function () {
      const uint8 = new Uint8Array([0x99]);
      const data = unpack('>B', uint8);
      expect(data[0]).to.equal(153);
    });
  
    it("Should unpack big endian signed short", function () {
      const uint8 = new Uint8Array([0x99, 0x02]);
      const data = unpack('>h', uint8);
      expect(data[0]).to.equal(-26365);
    });
  
    it("Should unpack big endian unsigned short", function () {
      const uint8 = new Uint8Array([0x99, 0x02]);
      const data = unpack('>H', uint8);
      expect(data[0]).to.equal(39170);
    });  
  
    it("Should unpack little endian signed short", function () {
      const uint8 = new Uint8Array([0x02, 0x99]);
      const data = unpack('<h', uint8);
      expect(data[0]).to.equal(-26365);
    });
  
    it("Should unpack little endian unsigned short", function () {
      const uint8 = new Uint8Array([0x02, 0x99]);
      const data = unpack('<H', uint8);
      expect(data[0]).to.equal(39170);
    });  
  
    it("Should unpack big endian signed int", function () {
      const uint8 = new Uint8Array([0x99, 0x99, 0x99, 0x02]);
      const data = unpack('>i', uint8);
      expect(data[0]).to.equal(-1717987069);
    });
 
    it("Should unpack big endian unsigned int", function () {
      const uint8 = new Uint8Array([0x99, 0x99, 0x99, 0x02]);
      const data = unpack('>I', uint8);
      expect(data[0]).to.equal(2576980226);
    }); 
  
  
    it("Should unpack little endian signed int", function () {
      const uint8 = new Uint8Array([0x02, 0x99, 0x99, 0x99]);
      const data = unpack('<i', uint8);
      expect(data[0]).to.equal(-1717987069);
    });
 
    it("Should unpack little endian unsigned int", function () {
      const uint8 = new Uint8Array([0x02, 0x99, 0x99, 0x99]);
      const data = unpack('<I', uint8);
      expect(data[0]).to.equal(2576980226);
    });   
  
    it("Should unpack big endian data", function () {
      const uint8 = new Uint8Array([0x01, 0x00, 0x02, 0x00, 0x00, 0x00, 0x03]);
      const data = unpack('>bhl', uint8);
      expect(data).to.equal([1, 2 ,3]);
    });

});

describe('parse_lscr test', function() {
  var tests = [
    {args: ['constants.Lnam', 'constants.Lscr'], expected: 'constants.js'},
    {args: ['local_var.Lnam', 'local_var.Lscr'], expected: 'local_var.js'}
    , 
  ];

  tests.forEach(function(test) {
    it('correctly decompiles ' + test.args[1] + ' file', function() {
      const lnamData = fs.readFileSync(path.resolve(__dirname, 'files', 'lingo', test.args[0]), 'utf8');
      const lsrcData = fs.readFileSync(path.resolve(__dirname, 'files', 'lingo', test.args[1]), 'utf8');
      const jsData = fs.readFileSync(path.resolve(__dirname, 'files', 'lingo', test.expected), 'utf8');

      var nameList = parse_lnam_file_data(lnamData);
      var script = parse_lrcr_file_data(lsrcData, nameList);

      var generated = generate_js_code(script);
      expect(generated).to.equal(jsData);
    });
  });
 });