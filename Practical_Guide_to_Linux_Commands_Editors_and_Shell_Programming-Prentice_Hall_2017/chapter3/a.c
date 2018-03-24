int		main(int ac, char **av)
{
  char		d;
  //  printf("%s\n", av[1]);
  my_putchar('a');
  my_putchar('\n');

  d = 0;
  while(d != 'EOF')
    {
      read(1, &d, 1);
      my_putchar(d);
    }
}

void		my_putchar(char c)
{
  write(1, &c, 1);
}
