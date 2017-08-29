var csrftoken = Cookies.get("csrftoken");
new Vue({
    el: '#editor',
    data:{
        value: '',
    },
    methods:{
        $save(value,render){
            axios({
                    method:'post',
                    url:'/admin/article/do_add',
                    headers:{'X-CSRFToken':csrftoken,'Content-Type':'application/x-www-form-urlencoded','X-Requested-With':'XMLHttpRequest'},
                    data:Qs.stringify({content:value})
                })
                .then(function(response){
                    console.log(response.data.msg);
                    alert(response.data.msg);
                })
                .catch(function(error){console.log(error)});
        } 
    }
});
