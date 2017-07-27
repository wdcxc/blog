var Vue = require('vue')
var mavonEditor = require('mavon-editor')
import 'mavon-editor/dist/css/index.css'

Vue.use(mavonEditor)
new Vue({
    'el': '#editor',
    data() {
        return { value: ''  }
    }
})
