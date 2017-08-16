/**
 * @Author: HuaChao Chen <CHC>
 * @Date:   2017-05-07T22:35:31+08:00
 * @Email:  chenhuachaoxyz@gmail.com
 * @Filename: index.js
 * @Last modified by:   CHC
 * @Last modified time: 2017-05-16T22:40:54+08:00
 * @License: MIT
 * @Copyright: 2017
 */

/*
options中若其属性值为false或者undefined，则代表默认按照由_two覆盖_own的值
options中若其属性值为true，则代表保留左边的第一个非空的值
 */

/**
 * merge operation
 * @param  {object} _one    need to merge
 * @param  {Object} _two    need to merge
 * @param  {Object} options options for merge method
 * @param  {Number} level   merge level
 * @return {Object}         the result of merge
 */
function _merge(_one, _two, options, level){
    if (options === undefined) options = {}
    // 递归处理
    for (var _ in _two) {
        // 若_one不存在这个元素，直接赋值
        if (_one[_] === undefined) _one[_] = _two[_];
        // 若配置按默认右边元素优先覆盖，则覆盖，若level>=0的话则不处理，因为>=0的话代表始终保留左值
        else if (options[_] === undefined || options[_] === false) level >= 0 ? null:_merge(_one[_], _two[_], options[_], level - 1);
        // 保留左值，因此不处理
        else if (options[_] === true) continue;
        else _merge(_one[_], _two[_], options[_], level - 1);
    }
    return _one;
}

/**
 * global merge function
 * @param  {Array} need    need to merge
 * @param  {Object} options options for merge method
 * @param  {Number} level  merge level
 * @return {Object}         the result of merges
 */
function merge(need, options, level){
    // 如果没有传第三个参数，默认无限递归右边覆盖左边
    if (level == undefined) level = -1;
    if (options === undefined) options = {};
    if (need.length == 1) return need[0];
    var res = {};
    for (var i = 0; i < need.length; i++){
        _merge(res, need[i], options, level - 1);
    }
    return res;
}

module.exports = merge
