/**
 * @Author: HuaChao Chen <CHC>
 * @Date:   2017-05-04T23:21:48+08:00
 * @Email:  chenhuachaoxyz@gmail.com
 * @Filename: webpack.dev.js
 * @Last modified by:   CHC
 * @Last modified time: 2017-06-18T23:32:44+08:00
 * @License: MIT
 * @Copyright: 2017
 */

var base = require('./webpack.base.js')
var merge = require('merges-utils')
var path = require('path');
var webpack = require('webpack');
var config = {
    entry: {
        mavon_editor: path.resolve(__dirname, './index.js')
    },
    output: {
        path: path.resolve(__dirname,'../../webpack_bundles/mavon-editor'),
        // publicPath: '/dist/',
        filename: '[name].js',
        chunkFilename: '[name].js',
        library: 'mavon-editor',
        libraryTarget: 'umd',
        umdNamedDefine: true
    },
    resolve: {
        alias: {
            'muse-components': 'muse-ui/src'
        },
        extensions: ['.js', '.vue', '.less']
    },
    externals: {
        vue: {
            root: 'Vue',
            commonjs: 'vue',
            commonjs2: 'vue',
            amd: 'vue'
        }
    }
}

var res = merge([base, config])
res.plugins = res.plugins.concat([
    new webpack.optimize.UglifyJsPlugin({
        compress: {
            warnings: false
        },
        comments: false
    })
])
module.exports = res
