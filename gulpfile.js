var gulp = require('gulp');
var concat = require('gulp-concat');
var sass   = require('gulp-sass');
var minifyCss = require('gulp-minify-css');
var STATIC_DEV = "./static-dev/";

gulp.task('scripts', function() {
  return gulp.src([
  		'lib/jquery/dist/jquery.js', 
  		'lib/bootstrap-sass-official/assets/javascripts/bootstrap.min.js', 
  		'lib/modernizr/modernizr.js', 
  		], {cwd: STATIC_DEV})
    .pipe(concat('scripts.js'))
    .pipe(gulp.dest('./static/'));
});

gulp.task('sass', function() {
  return gulp.src(STATIC_DEV + 'scss/main.scss')
  	.pipe(sass())
    .pipe(minifyCss())
    .pipe(gulp.dest('./static/'))
});

gulp.task('default', ['sass', 'scripts'], function() {
    gulp.watch([STATIC_DEV + '**/*.scss', STATIC_DEV + '**/*.js'], ['sass', 'scripts']);
});