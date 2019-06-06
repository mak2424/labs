#include <getopt.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef void (*test_case)(void);

extern test_case test_cases[];

static void run_test_suite(int start_idx) {
  for (int i = 0; test_cases[i] != NULL; i++) {
    if (i < start_idx)
      continue;
    fprintf(stderr, "Running test #%d...\n", i);
    (*test_cases[i])();
  }
  fprintf(stderr, "Done testing.\n");
}

double longrunning_rotation(void);
double longrunning_flipcount(void);

void print_usage(const char *argv_0)
{
    fprintf(stderr, "usage: %s\n"
      "\t -t 0\tRun test suite, starting from the first test\n"
      "\t -r\tRun a sample long-running rotation operation\n"
      "\t -f\tRun a sample long-running flip count operation\n"
      , argv_0);
}

int main(int argc, char **argv) {
  char optchar;
  opterr = 0;
  while ((optchar = getopt(argc, argv, "t:rf")) != -1) {
    switch (optchar) {
      case 't':
        run_test_suite(atoi(optarg));
        return EXIT_SUCCESS;
        break;
      case 'r':
        printf("---- RESULTS ----\n");
        printf("Elapsed execution time: %.6fs\n", longrunning_rotation());
        printf("---- END RESULTS ----\n");

        return EXIT_SUCCESS;
        break;
      case 'f':
        printf("---- RESULTS ----\n");
        printf("Elapsed execution time: %.6fs\n", longrunning_flipcount());
        printf("---- END RESULTS ----\n");

        return EXIT_SUCCESS;
        break;
    }
  }
  print_usage(argv[0]);
}
