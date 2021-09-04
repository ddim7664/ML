public void shellsort(integer[]arr){

    int interval = arr.length/2;

    while (interval! = 0) {
        for(int i = 0; i < interval; i++){
            for(int p = i + interval; p< arr.length;p+=interval){

                int key = arr[p];
    int j = p - interval;
    while(j>=0){
        if (key < arr[i]){
            arr[j + inaterval] = arr[j]
        } else
            break;
        j -=interval;

    }
    arr[j + interval;] = key;

}
    interval /= 2;

}
}








}