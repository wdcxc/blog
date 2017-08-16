new Vue({
    el: '#editor',
    data:{
        value: ''
    },
    methods:{
        $save(value,render){
            alert(value);
        } 
    }
});
