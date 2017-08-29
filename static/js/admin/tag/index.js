var csrftoken = Cookies.get("csrftoken");
new Vue({
    el:"#tags_table",
    methods:{
        increaseGrade:function(id,type){
            axios({
                method:"POST",
                url:"/admin/tag/change_grade",
                headers:{"X-CSRFToken":csrftoken,"X-Requested-With":"XMLHttpRequest","Content-Type":"application/x-www-form-urlencoded"},
                data:Qs.stringify({id:id,'type':type})
            })
                .then(function(response){
                    alert(response.data.msg);
                    location.reload();
                })
            .catch(function(error){alert(error)})
        },
        decreaseGrade:function(id,type){
            axios({
                method:"POST",
                url:"/admin/tag/change_grade",
                headers:{"X-CSRFToken":csrftoken,"X-Requested-With":"XMLHttpRequest","Content-Type":"application/x-www-form-urlencoded"},
                data:Qs.stringify({id:id,'type':type})
            })
                .then(function(response){
                    alert(response.data.msg);
                    location.reload();
                })
            .catch(function(error){alert(error)})
        },
        changeShow:function(id,$event){
            axios({
                method:"POST",
                url:"/admin/tag/change_show",
                headers:{"X-CSRFToken":csrftoken,"X-Requested-With":"XMLHttpRequest","Content-Type":"application/x-www-form-urlencoded"},
                data:Qs.stringify({id:id,'show':Number($event.target.checked)})
            })
                .then(function(response){
                    alert(response.data.msg);
                    location.reload();
                })
            .catch(function(error){alert(error)})
        },
    }
});
