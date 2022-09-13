// importing functions
// for docs refer to scraper.ts
import {get_professor, get_all_professor} from './scraper'

// test code
const name = 'kevin chun'
const ret = get_professor(name)

ret.then(function(r) {
    console.log(r)
})