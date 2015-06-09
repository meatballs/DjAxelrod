var gulp = require('gulp');
var concat = require('gulp-concat');
var sass   = require('gulp-sass');
var minifyCss = require('gulp-minify-css');


var STATIC_DEV = "./static-dev/";
var STATIC = './static/';

gulp.task('scripts', function() {
  return gulp.src([
  		'lib/jquery/dist/jquery.js',
  		'lib/d3/d3.min.js',
  		'lib/colorbrewer/colorbrewer.js',
  		'lib/bootstrap-sass-official/assets/javascripts/bootstrap.min.js',
      'lib/bootstrap-multiselect/dist/js/bootstrap-multiselect.js',
  		'lib/modernizr/modernizr.js',
      'js/vis.js',
  		'js/main.js',
  		], {cwd: STATIC_DEV})
    .pipe(concat('scripts.js'))
    .pipe(gulp.dest(STATIC));
});

gulp.task('sass', function() {
  return gulp.src(STATIC_DEV + 'scss/main.scss')
  	.pipe(sass())
    .pipe(minifyCss())
    .pipe(gulp.dest(STATIC));
});

gulp.task('favicon', function(){
  return gulp.src(STATIC_DEV + 'favicon.ico').pipe(gulp.dest(STATIC));
});

// remove all the csv stuff after we add in the csv api
gulp.task('csv', function() {
  return gulp.src(STATIC_DEV + 'csv/*.csv').pipe(gulp.dest(STATIC));
});

gulp.task('default', ['sass', 'scripts', 'favicon', 'csv'], function() {
    gulp.watch([STATIC_DEV + '**/*.scss', STATIC_DEV + '**/*.js', STATIC_DEV + '**/*.csv'], ['sass', 'scripts', 'csv']);
});
