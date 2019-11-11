var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var ExtractText = require('extract-text-webpack-plugin');
var WriteFilePlugin = require('write-file-webpack-plugin');

module.exports = {
    mode:           'development',
    context:        __dirname,
    entry: [
        'react-hot-loader/patch',
        'webpack-dev-server/client?http://localhost:3000',
        'webpack/hot/only-dev-server',
        './src/index',
    ],
    output: {
        path:       path.resolve('./static/js'),
        filename:   '[name]-[hash].js',
        //publicPath: '/static/js/',
        publicPath: 'http://localhost:3000/static/js/'
    },
    plugins: [
        new WriteFilePlugin(),
        new webpack.HotModuleReplacementPlugin(),
        new webpack.NoEmitOnErrorsPlugin(), // don't reload if there is an error
        new BundleTracker({
            path: __dirname,
            filename: './webpack-stats.json'
        }),
        new ExtractText({
            filename: '[name]-[hash].css'
        }),
    ],
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: ['babel-loader'],
            },
            {
                test: /\.js$/,
                include: /node_modules\/react-lifecycles-compat/,
                use: ['babel-loader'],
            },
            {
                test: /\.jsx?$/,
                exclude: /node_modules\/react-dom/,
                use: {
                    loader: 'react-hot-loader/webpack',
                    options: {
                        noRegister: true,
                    },
                }
            },
            {
                test: /\.css$/,
                loader: ['style-loader', 'css-loader'],
            },
            {
                test: /\.scss$/,
                use: ExtractText.extract({
                    fallback: 'style-loader',
                    use: ['css-loader', 'sass-loader']
                })
            },
            {
                test: /\.(woff(2)?|ttf|eot|svg)(\?v=\d+\.\d+\.\d+)?$/,
                use: [{
                        loader: 'file-loader',
                        options: {
                            name: '[name].[ext]',
                            outputPath: 'fonts/'
                        }
                }]
            },
            {
                test: /\.(png|jp(e*)g|svg)$/,
                use: [{
                    loader: 'url-loader',
                    options: {
                        limit: 25000, // Convert images < 8kb to base64 strings
                        name: '[hash]-[name].[ext]',
                        outputPath: 'images/'
                    }
                }]
            }
        ],
    },

    resolve: {
        //modulesDirectories: ['node_modules', 'bower_components'],
        extensions: ['*', '.js', '.jsx']
        //extensions: ['', '.js', '.jsx']
    },
}
