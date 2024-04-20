import { compress, decode, decompress } from './core'
import { trimUndefined, trimUndefinedRecursively } from './helpers'
import { addValue } from './memory'

const compressJSON = {
  compress,
  decompress,
  decode,
  addValue,
  trimUndefined,
  trimUndefinedRecursively,
}

export default compressJSON
Object.assign(window, { compressJSON })
