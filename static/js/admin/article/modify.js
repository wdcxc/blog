var csrftoken = Cookies.get("csrftoken");
var id = document.getElementById("id").value;
var content = document.getElementById("content").value;
var meta = document.getElementById("meta").value;
var article = meta + '\n' + content;
new Vue({
    el: '#editor',
    data:{
        id: id,
        value: article,
    },
    methods:{
        $save(value,render){
            $(".ui.modal").modal("show");
            $(".markdown-body").css("z-index","1");
            axios({
                    method:'post',
                    url:'/admin/article/do_modify',
                    headers:{'X-CSRFToken':csrftoken,'Content-Type':'application/x-www-form-urlencoded','X-Requested-With':'XMLHttpRequest'},
                    data:Qs.stringify({id:this.id,content:value})
                })
                .then(function(response){
                    console.log(response);
                    alert(response.data.msg);
                    $(".ui.modal").modal("hide");
                })
                .catch(function(error){
                    console.log(error);
                    alert(error);
                    $(".ui.modal").modal("hide");
                });
        } 
    }
});
