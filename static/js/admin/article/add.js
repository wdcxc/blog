var csrftoken = Cookies.get("csrftoken");
new Vue({
    el: '#editor',
    data:{
        value: "---\ntitle: 文章标题\nauthor: 作者\ncategories: 类别1,类别2\ntags: 标签1,标签2\n---\n",
    },
    methods:{
        $save(value,render){
            $(".ui.modal").modal("show");
            $(".markdown-body").css("z-index",1);
            axios({
                    method:'post',
                    url:'/admin/article/do_add',
                    headers:{'X-CSRFToken':csrftoken,'Content-Type':'application/x-www-form-urlencoded','X-Requested-With':'XMLHttpRequest'},
                    data:Qs.stringify({content:value})
                })
                .then(function(response){
                    console.log(response.data.msg);
                    alert(response.data.msg);
                    $(".ui.modal").modal("hide");
                })
                .catch(function(error){
                    console.log(error);
                    $(".ui.modal").modal("hide");
                });
        } 
    }
});
