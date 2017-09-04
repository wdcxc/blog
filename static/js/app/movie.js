new Vue({
    el:"#search",
    data:{
        searchName:"",
    },
    methods:{
        doSearch:function(){
            window.location.href = "/app/movie?search_name="+this.searchName;
        }
    }
});
