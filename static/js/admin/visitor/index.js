var csrftoken = Cookies.get("csrftoken");
new Vue({
    el:"#visitorsTable",
    methods:{
        changeForbiddenVisit:function(id,$event){
            axios({
                method:"POST",
                url:"/admin/visitor/change_forbidden_visit",
                headers:{"X-CSRFToken":csrftoken,"X-Requested-With":"XMLHttpRequest","Content-Type":"application/x-www-form-urlencoded"},
                data:Qs.stringify({id:id,'forbidden_visit':Number($event.target.checked)})
            })
                .then(function(response){
                    alert(response.data.msg);
                    location.reload();
                })
            .catch(function(error){alert(error)})
        },
    }
});
