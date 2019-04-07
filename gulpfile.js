var gulp = require('gulp');
var runSequence = require('run-sequence');
var jshint = require('gulp-jshint');
var source = require('vinyl-source-stream');
var streamify = require('gulp-streamify');
var browserify = require('browserify');
var uglify = require('gulp-uglify');
var mocha = require('gulp-mocha');

gulp.task('default', function() {
    // place code for your default task here
});

gulp.task('lint', function() {
    return gulp.src(['./js/**/*.js', './test/**/*.test.js'])
        .pipe(jshint())
        .pipe(jshint.reporter('default'));
});

// Watch Files For Changes
gulp.task('watch', function() {
    gulp.watch('js/**/*.js', ['lint', 'scripts']);
});

gulp.task('scripts', function() {
    var bundleStream = browserify('./js/app.js', { entry: true, debug: true }).bundle();

    bundleStream
        .pipe(source('./js/app.js'))
        .pipe(gulp.dest('./build'))
});

gulp.task('scripts-prod', function() {
    var bundleStream = browserify('./js/app.js').bundle();

    bundleStream
        .pipe(source('./js/app.js'))
        .pipe(streamify(uglify()))
        .pipe(gulp.dest('./build'))
});

gulp.task('mocha', function () {
    return gulp.src('./test/**/*.test.js', {read: false})
        .pipe(mocha({reporter: 'spec'}));
});

gulp.task('test', function(){
    runSequence('mocha', 'lint');
});