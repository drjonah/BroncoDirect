// importing functions
// for docs refer to scraper.ts
import {getProfessor, getAllProfessor} from './scraper'

// test code
const name = 'ofoiwfoiwfiwfij'
const ret = getProfessor(name)

ret.then(function(r) {
  console.log(r)
})
