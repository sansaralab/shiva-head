function println(data) {
    if (typeof console !== 'undefined') {
        console.log(data);
    }
}


module.exports = {
    println: println
};
