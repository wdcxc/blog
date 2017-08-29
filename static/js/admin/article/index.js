var csrftoken = Cookies.get("csrftoken");

var articlesTable = new Vue({
    el:'#articlesTable',
    methods:{
        deleteArticle:function(id){
            axios({
                    method:"POST",
                    url:"/admin/article/delete",
                    headers:{"X-CSRFToken":csrftoken,"X-Requested-With":"XMLHttpRequest","Content-Type":"application/x-www-form-urlencoded"},
                    data:Qs.stringify({id:id})
                })
                .then(function(response){
                    alert(response.data.msg);
                    console.log(response);
                    location.reload();
                })
                .catch(function(error){
                    alert(error);
                    console.log(error);
                });
        },
        openToPublic:function(id,open){
            axios({
                    method:"POST",
                    url:"/admin/article/open_to_public",
                    headers:{"X-CSRFToken":csrftoken,"X-Requested-With":"XMLHttpRequest","Content-Type":"application/x-www-form-urlencoded"},
                    data:Qs.stringify({id:id,open:open})
                })
                .then(function(response){
                    alert(response.data.msg);
                    if(response.data.code==200){
                        location.reload();
                    }    
                })
                .catch(function(error){
                    alert(error);
                    console.log(error);
                });
        },
        previousPage:function(page){
            if(location.href.indexOf("?")!=-1){
                if(location.href.indexOf("page")!=-1){
                    location.href = location.href.replace(/page=\d+/,"page="+page)
                }else{
                    location.href += "&page=" + page;
                }
            }else{
                if(location.href.indexOf("page")!=-1){
                    location.href = location.href.replace(/page=\d+/,"page="+page)
                }else{
                    location.href += "?page=" + page;
                }
            }
        },
        nextPage:function(page){
            if(location.href.indexOf("?")!=-1){
                if(location.href.indexOf("page")!=-1){
                    location.href = location.href.replace(/page=\d+/,"page="+page)
                }else{
                    location.href += "&page=" + page;
                }
            }else{
                if(location.href.indexOf("page")!=-1){
                    location.href = location.href.replace(/page=\d+/,"page="+page)
                }else{
                    location.href += "?page=" + page;
                }
            }
        }
    }
});

var searchCondition = "title";

var searchInput = new Vue({
    el:"#searchInput",
    data:{
        searchText:"",
    },
    methods:{
        search:function(){
            location.href = "/admin/article/index?search=true&search_condition="+searchCondition+"&search_text="+this.searchText;
        }
    }
});
