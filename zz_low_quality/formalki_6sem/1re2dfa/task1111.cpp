#include "api.hpp"
#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <iostream>
#include <algorithm>

bool check_sym(char str) {
    if (str == '|') return false;
    if (str == '(') return false;
    if (str == ')') return false;
    if (str == '*') return false;
    if (str == '.') return false;
    return true;
  }

  void poliz_or (std::string&, std::string, int&);
  void poliz_and (std::string&, std::string, int&);
  void poliz_sym (std::string&, std::string, int&);

void poliz_or (std::string &poliz, std::string str, int &i) {
    poliz_and(poliz, str, i);
    while (str[i] == '|') {
        i++;
        poliz_and(poliz, str, i);
        poliz.append(1, '|');
    }
    return;
}
 
void poliz_and(std::string& poliz, std::string str, int& i) {
    poliz_sym(poliz, str, i);
    //std::cout << str[i] << i << std::endl;
    while (str[i] == '.') {
        i++;
        poliz_sym(poliz, str, i);
        poliz.append(1, '.');
    }
    return;
}

 
void poliz_sym (std::string& poliz, std::string str, int& i) {
    if (str[i] == '(' )  {
        i++;
        poliz_or(poliz, str, i);
        if (str[i] == ')' )
            i++;
            if (str[i] == '*' )
            {
              poliz.append(1, '*');
              i++;
            }
    }
    else {
        poliz.append(1, str[i]);
        i++;
        if (str[i] == '*' )
            {
              poliz.append(1, '*');
              i++;
            }
}
return;
}

std::string num_to_str(int x)
{
  int d, p;
  std::string str;
  if (x == 0)
    return "0";
  while (x != 0)
  {
    p = x % 10;
    str.append(1, (char)(p + 48));
    x = x / 10;
  }
  reverse(str.begin(),str.end());
  return str;
}

DFA re2dfa(const std::string &s) {

	//std::cout << "hi";
	std::string alp = Alphabet(s).to_string();
	DFA res = DFA(Alphabet(s));
	std::string line = s;
	std::string str = s;

	char pred_sym = str[0];
  line.insert(line.length(), "#");

  str.insert(str.length(), "#");

  int pos = 0;

  int i;

  for (i=0; i<line.length() ; i++)
  {
    if (check_sym(line[i]))
    {
      pos++;
    }
  }

	i = 1;
  while (line[i] != '#')
  {
	if ((pred_sym == '(') && (str[i] == '|'))
        {
        pred_sym = str[i];
		str.insert(i, "$");
        i = i + 2;
        }
    else if ((pred_sym == '|') && (str[i] == ')'))
        {
        pred_sym = str[i];
		str.insert(i, "$");
        i = i + 2;
        }
	else if ((pred_sym == '(') && (str[i] == ')'))
        {
        pred_sym = str[i];
        str.insert(i, "$");
        i = i + 2;
        }
	else 
	{
		pred_sym = line[i];
		i++;
	}
  }

	pred_sym = line[0];

  i = 1;
  while (line[i] != '#')
  {
    if ((check_sym(line[i]) == check_sym(pred_sym)) && (check_sym(line[i]) == true))
    {
      pred_sym = line[i];
      line.insert(i, ".");
      i = i + 2;
    }
    else if ((pred_sym == '(') && (line[i] == '|'))
        {
        pred_sym = line[i];
        line.insert(i, "$");
        i = i + 2;
        }
	else if ((pred_sym == '|') && (i == 1))
        {
        pred_sym = line[i];
        line.insert(i - 1, "$");
        i = i + 2;
        }
    else if ((pred_sym == '|') && (line[i] == ')'))
        {
        pred_sym = line[i];
        line.insert(i, "$");
        i = i + 2;
        }
    else if ((pred_sym == ')') && (line[i] == '('))
        {
        pred_sym = line[i];
        line.insert(i, ".");
        i = i + 2;
        }
    else if ((pred_sym == ')') && (check_sym(line[i]) == true))
        {
        pred_sym = line[i];
        line.insert(i, ".");
        i = i + 2;
        }
    else if ((pred_sym == '*') && (check_sym(line[i]) == true))
        {
        pred_sym = line[i];
        line.insert(i, ".");
        i = i + 2;
        }
	else if ((line[i] == '(') && (check_sym(pred_sym) == true))
        {
        pred_sym = line[i];
        line.insert(i, ".");
        i = i + 2;
        }
    else if ((pred_sym == '(') && (line[i] == ')'))
        {
        pred_sym = line[i];
        line.insert(i, "$");
        i = i + 2;
        }
    else if ((pred_sym == '*') && (line[i] == '('))
        {
        pred_sym = line[i];
        line.insert(i, ".");
        i = i + 2;
        }
    else 
    {
      pred_sym = line[i];
      i++; 
    }
  }


  str.pop_back();

  //std::cout << str << std::endl;


  



  //std::cout << line;

  //std::cout << std::endl;

  i = 0;

  std::string poliz;
  poliz_or(poliz, line, i);

  //std::cout << poliz << std::endl;

  poliz.append(1, '#');
  poliz.append(1, '.');
  std::cout << poliz << std::endl;


  std::string nullable;

  /*char u = poliz[0];
  char v;*/




  std::vector <std::set <int > > firstpos(poliz.length());

  std::vector <std::set <int > > lastpos(poliz.length());

  std::vector <std::set <int > > followpos(pos);

  std::vector <char > tabl(pos);


  int u2;

  int v2;

  std::stack <int> st;

  char pred = poliz[0];

  int k = 1;
  for (i=0; i<poliz.length() ; i++)
  {
    if (poliz[i] == '*')
    {
      nullable.append(1, 't');
      for(auto j : firstpos[st.top()])
        firstpos[i].insert(j);
      for(auto j : lastpos[st.top()])
        lastpos[i].insert(j);
      st.pop();
      st.push(i);
      for(auto j : lastpos[st.top()])
        for(auto x : firstpos[st.top()])
          followpos[j].insert(x);
    }
    else if (poliz[i] == '|')
    {
      v2 = st.top();
      st.pop();
      u2 = st.top();
      st.pop();
      if ((nullable[u2] == 't') || (nullable[v2] == 't')) 
        nullable.append(1, 't');
      else
        nullable.append(1, 'f');
	  if (poliz[v2] == '$') 
	  {
		if (poliz[u2] == '$');
		else
		{
			for(auto j : firstpos[u2])
        		firstpos[i].insert(j);
			for(auto j : lastpos[u2])
        		lastpos[i].insert(j);
		}
	  }
	  else if (poliz[u2] == '$')
	  {
	  	if (poliz[v2] == '$');
		else
		{
			/*for(auto j : firstpos[v2])
        		std::cout << "fv2  " << i << std::endl;
      		for(auto j : lastpos[v2])
        		std::cout << "lv2  " << j << std::endl;*/
			for(auto j : firstpos[v2])
        		firstpos[i].insert(j);
      		for(auto j : lastpos[v2])
        		lastpos[i].insert(j);
		}
	  }
	  else 
	  { 
		for(auto j : firstpos[u2])
        	firstpos[i].insert(j);
		for(auto j : lastpos[u2])
        	lastpos[i].insert(j);
      	for(auto j : firstpos[v2])
        	firstpos[i].insert(j);
      	for(auto j : lastpos[v2])
        	lastpos[i].insert(j);
	  }
      st.push(i);
    }
    else if (poliz[i] == '.')
    {
      v2 = st.top();
      st.pop();
      u2 = st.top();
      st.pop();
      if ((nullable[u2] == 't') && (nullable[v2] == 't')) 
        nullable.append(1, 't');
      else
        nullable.append(1, 'f');
      if (nullable[u2] == 't')
      {
        for(auto j : firstpos[v2])
          firstpos[i].insert(j);
        for(auto j : firstpos[u2])
          firstpos[i].insert(j);
      }
      else
      {
        for(auto j : firstpos[u2])
          firstpos[i].insert(j);
      }
      if (nullable[v2] == 't')
      {
        for(auto j : lastpos[v2])
          lastpos[i].insert(j);
        for(auto j : lastpos[u2])
          lastpos[i].insert(j);
      }
      else
      {
        for(auto j : lastpos[v2])
          lastpos[i].insert(j);
      }
      st.push(i);
      for(auto j : lastpos[u2])
        for(auto x : firstpos[v2])
          followpos[j].insert(x);
    }
    else if (poliz[i] == '$')
    {
      nullable.append(1, 't');
      st.push(i);
      k++;
    }
    else
    {
      nullable.append(1, 'f');
      firstpos[i].insert(k);
      lastpos[i].insert(k);
      k++;
      st.push(i);
    }
  }

 std::cout << nullable << std::endl;


  for (int j=0; j<poliz.length(); j++)
  {
    for(auto i : firstpos[j])
        std::cout << i;
    std::cout << std::endl;
    for(auto i : lastpos[j])
    	std::cout << i;
    std::cout << std::endl;
    std::cout << "********************" << std::endl;
  }

  std::cout << "////////////////////////////////////////////" << std::endl;


  for (int j=0; j<pos; j++)
  {
    for(auto i : followpos[j])
        std::cout << i;
    std::cout << std::endl;
  }

  std::set <int> q0 = firstpos[poliz.length() - 1];


  std::vector <std::set <int> > cond;

  //std::cout << std::endl << "xxxxxxx" << std::endl;

  i = 1;

	for (int j=0; j<line.length(); j++)
	{
		if (check_sym(line[j]))
		{
			tabl[i] = line[j];
			i++;
		}
	}




	cond.push_back(q0);

	bool fin = false;

	std::string pred_cond = "";

	std::string name = "";
	for(auto i : cond)
	{
		for(auto j : i)
			{
				if (j == pos)
					fin = true;
        		name.append(1, (char)(j + 48));
			}
		//std::cout << name;
		if (fin)
				{
					res.create_state("0", true);
					fin = false;
				}
				else
					res.create_state("0", false);
		res.set_initial(name);
		name = "";
	}



	std::string tmp;

	std::string tmp2;

	std::set <int> q_next;

	int index = 0;

	fin = false;

  int ind1 = 0;
  int ind2 = 0;
 

	//for(auto i : cond)

  for (i = 0; i < cond.size(); i++)
	{
		for(auto p : cond[i])
    {
				pred_cond.append(1, (char)(p + 48));
        //std::cout << p; 
    }
    std::cout << std::endl;
		for(auto t : alp)
		{
      std::cout << "curr state " << pred_cond << std::endl; 
			std::cout << "alphavit " << t << std::endl; 
      for(auto j : cond[i])
				std:: cout << j;
      std::cout << std::endl;
			for(auto k : cond[i])
			{
				if (t == tabl[k])
				{
					std::cout << "tabl[k] " << tabl[k] << std::endl; 
					for (auto c : followpos[k])
					{
						std::cout << "followpos[k] " << c << ' ' << k << std::endl;
						q_next.insert(c);
						if (c == pos)
							fin = true;
					}
				}
				index++;
			}
			for(auto p : q_next)
				tmp.append(1, (char)(p + 48));
			name.append(1, (char)(index + 48));
      std::vector <std::set <int> > ::iterator it = std:: find ( cond.begin(), cond.end(), q_next);
      ind2 = std::distance(cond.begin(), it);
     if (it != cond.end())
      {
        it = std:: find ( cond.begin(), cond.end(), cond[i]);
        ind1 = std::distance(cond.begin(), it);
      }
      else
      {
        it = std:: find ( cond.begin(), cond.end(), cond[i]);
        ind1 = std::distance(cond.begin(), it);
        cond.push_back(q_next);
      }
			if (tmp != "")
			{
				if (fin)
				{
					res.create_state(num_to_str(ind2), true);
					fin = false;
				}
				else
					res.create_state(num_to_str(ind2), false);
				std::cout << "pred_cond and tmp " << num_to_str(ind1) << ' ' << num_to_str(ind2) << std::endl;
				res.set_trans(num_to_str(ind1), t, num_to_str(ind2));
			}
			tmp = "";
      std::cout <<  k << std::endl;
			
			q_next.clear();
			name = "";

		}
		pred_cond = "";
	}

  

	return res;
}