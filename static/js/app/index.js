new Vue({
    el:"#articles_cards",
    method:{
        goToTag:function(tag_id){
            location.href = "/app/tag?id="+tag_id;
        }
    }
});
