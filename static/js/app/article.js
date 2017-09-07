var csrftoken = Cookies.get('csrftoken');

Vue.component('comment-component',{
    template: '#comment-component',
    props:['commentid','articleid'],
    data:function(){
        return {
            formShow:false,
            commentContent:'',
            content:'',
            comment:{},
            visitor:{},
            commentIds:[],
            submitLoading:false,
        }
    },
    computed:{
        hasComments:function(){ return this.commentIds && this.commentIds.length }
    },
    mounted:function(){
        var that = this;
        axios({
            url:'/app/get_comment',
            method:'post',
            headers:{'Content-Type':'application/x-www-form-urlencoded','X-Request-With':'XMLHttpRequest','X-CSRFToken':csrftoken},
            data:Qs.stringify({comment_id:this.commentid})
        })
        .then(function(response){
            console.log(response);
            if(response.data.code == 200){ 
                that.comment = JSON.parse(response.data.data.comment);
                that.visitor = JSON.parse(response.data.data.visitor);
                that.commentIds = response.data.data.comment_ids;
            }
        })
        .catch(function(error){
            console.log(error);
        })
    },
    watch:{
        commentid:function(){
            var that = this;
            axios({
                url:'/app/get_comment',
                method:'post',
                headers:{'Content-Type':'application/x-www-form-urlencoded','X-Request-With':'XMLHttpRequest','X-CSRFToken':csrftoken},
                data:Qs.stringify({comment_id:this.commentid})
            })
            .then(function(response){
                console.log(response);
                if(response.data.code == 200){ 
                    that.comment = JSON.parse(response.data.data.comment);
                    that.visitor = JSON.parse(response.data.data.visitor);
                    that.commentIds = response.data.data.comment_ids;
                }
            })
            .catch(function(error){
                console.log(error);
            })
        }
    },
    methods:{
        showReplyForm:function(){
            this.formShow = !this.formShow;
        },
        replyComment:function(commentId,visitorId,articleId){
            var that = this;
            this.submitLoading=true;
            axios({
                    url:'/app/add_comment',
                    method:'post',
                    headers:{'Content-Type':'application/x-www-form-urlencoded','X-Request-With':'XMLHttpRequest','X-CSRFToken':csrftoken},
                    data:Qs.stringify({comment_id:commentId,visitor_id:visitorId,comment_content:this.commentContent})
            })
            .then(function(response){
                console.log(response);
                alert(response.data.msg);
                that.submitLoading=false;
                if(response.data.code == 200){ 
                    that.commentIds.unshift(response.data.data.comment_id); 
                    that.commentContent = '';
                    that.formShow = !that.formShow;
                }
            })
            .catch(function(error){
                that.submitLoading=false;
                console.log(error);
            })
        }
    }
});

var comments = new Vue({
    el:"#comments",
    data:{
        commentContent:'', 
        commentIds:[],
        articleId:$("#articleId").val(),
        submitLoading:false,
    },
    mounted:function(){
        var that = this;
        axios({
            url:'/app/get_comment',
            method:'post',
            headers:{'Content-Type':'application/x-www-form-urlencoded','X-Request-With':'XMLHttpRequest','X-CSRFToken':csrftoken},
            data:Qs.stringify({article_id:this.articleId})
        })
        .then(function(response){
            console.log(response);
            if(response.data.code == 200){ 
                that.commentIds = response.data.data.comment_ids;
            }
        })
        .catch(function(error){
            console.log(error);
        })
    },
    methods:{
        articleComment:function(visitorId,articleId){
            var that = this;
            this.submitLoading=true;
            axios({
                    url:'/app/add_comment',
                    method:'post',
                    headers:{'Content-Type':'application/x-www-form-urlencoded','X-Request-With':'XMLHttpRequest','X-CSRFToken':csrftoken},
                    data:Qs.stringify({article_id:articleId,visitor_id:visitorId,comment_content:this.commentContent})
            })
            .then(function(response){
                console.log(response);
                alert(response.data.msg);
                that.submitLoading=false;
                if(response.data.code == 200){ 
                    that.commentIds.unshift(response.data.data.comment_id); 
                    that.commentContent = '';
                }
            })
            .catch(function(error){
                that.submitLoading=false;
                console.log(error);
            })
        }
    }
});
