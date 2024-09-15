# C++ File Management

## Create directory
```C
mkdir(download_dir, 0777)
// if (mkdir(download_dir, 0777) == -1) {
//         perror("Error creating directory");
//         exit(EXIT_FAILURE);
//     }
```

## Cd to directory
```C
chdir(links_dir) == -1
// if (chdir(links_dir) == -1) {
//     perror("Error changing directory");
//     exit(EXIT_FAILURE);
// }
```

## Read file
```C
    FILE* numbers_file = fopen(numbers_filename, "r");
    // if (numbers_file == NULL) {
    //     perror("Error opening numbers file");
    //     exit(EXIT_FAILURE);
    // }

    for (int i = 0; i < SIZE; i++) {
        fscanf(numbers_file, "%lf", &numbers[i]);
        // if (fscanf(numbers_file, "%lf", &numbers[i]) != 1) {
        //     fprintf(stderr, "Error reading from file\n");
        //     exit(EXIT_FAILURE);
        // }
    }
    fclose(numbers_file);
```
## Write to file
```C
    FILE* file = fopen(filename, "w");
    // if (file == NULL) {
    //     perror("Error opening file");
    //     exit(EXIT_FAILURE);
    // }
    for (int i = 0; i < SIZE; i++) {
        double randomNumber = (double)rand() / RAND_MAX; // Generate a random number between 0 and 1
        fprintf(file, "%.2f\n", randomNumber);
    }
    fclose(file);
```