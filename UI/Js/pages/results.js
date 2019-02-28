const groupBy = (items, key) =>
  items.reduce(
    (result, item) => ({
      ...result,
      [item[key]]: [...(result[item[key]] || []), item]
    }),
    {}
  );

fetch("https://tevpolitico.herokuapp.com/api/v2/offices/metainfo")
  .then(data => data.json())
  .then(data => groupBy(data.data, "type"))
  .then(data => {
    console.log(data);
    let officetypelist = Object.keys(data);
    let vdom = {
      type: "div",
      props: {},
      children: officetypelist.map(type => ({
        type: "div",
        props: {},
        children: [
          {
            type: "h1",
            props: { class: "positiontitle" },
            children: [`Office-type: ${type}`]
          },
          {
            type: "div",
            props: {},
            children: data[type].map(office => ({
              type: "div",
              props: {},
              children: [
                {
                  type: "h3",
                  props: { class: "officename" },
                  children: [office.name]
                },
                {
                  type: "div",
                  props: {},
                  children:
                    office.candidates.length > 0
                      ? office.candidates.map(candidate => ({
                          type: "h3",
                          props: { class: "candidatesinfo" },
                          children: [
                            `${candidate.username} - Votes: ${candidate.result}`
                          ]
                        }))
                      : [
                          {
                            type: "h3",
                            props: { class: "candidatesinfo" },
                            children: [
                              "No One is vying in this post contact the admin if you are interested"
                            ]
                          }
                        ]
                }
              ]
            }))
          }
        ]
      }))
    };
    return vdom;
  })
  .then(vdom => {
    const $results = document.getElementById("results");
    $results.appendChild(createElement(vdom));
  });