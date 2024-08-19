const Table = () => {
  return (
    <div className="flex flex-col">
      <div className="-m-1.5 overflow-x-auto">
        <div className="inline-block min-w-full p-1.5 align-middle">
          <div className="overflow-hidden border dark:border-neutral-700">
            <table className="min-w-full divide-y divide-gray-200 dark:divide-neutral-700">
              <thead>
                <tr>
                  <th
                    scope="col"
                    className="px-6 py-3 text-start text-xs font-medium uppercase text-gray-500 dark:text-neutral-500"
                  >
                    Name
                  </th>
                  <th
                    scope="col"
                    className="px-6 py-3 text-start text-xs font-medium uppercase text-gray-500 dark:text-neutral-500"
                  >
                    Age
                  </th>
                  <th
                    scope="col"
                    className="px-6 py-3 text-start text-xs font-medium uppercase text-gray-500 dark:text-neutral-500"
                  >
                    Address
                  </th>
                  <th
                    scope="col"
                    className="px-6 py-3 text-end text-xs font-medium uppercase text-gray-500 dark:text-neutral-500"
                  >
                    Action
                  </th>
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-200 dark:divide-neutral-700">
                <tr>
                  <td className="whitespace-nowrap px-6 py-4 text-sm font-medium text-gray-800 dark:text-neutral-200">
                    John Brown
                  </td>
                  <td className="whitespace-nowrap px-6 py-4 text-sm text-gray-800 dark:text-neutral-200">
                    45
                  </td>
                  <td className="whitespace-nowrap px-6 py-4 text-sm text-gray-800 dark:text-neutral-200">
                    New York No. 1 Lake Park
                  </td>
                  <td className="whitespace-nowrap px-6 py-4 text-end text-sm font-medium">
                    <button
                      type="button"
                      className="inline-flex items-center gap-x-2 rounded-lg border border-transparent text-sm font-semibold text-blue-600 hover:text-blue-800 focus:text-blue-800 focus:outline-none disabled:pointer-events-none disabled:opacity-50 dark:text-blue-500 dark:hover:text-blue-400 dark:focus:text-blue-400"
                    >
                      Delete
                    </button>
                  </td>
                </tr>

                <tr>
                  <td className="whitespace-nowrap px-6 py-4 text-sm font-medium text-gray-800 dark:text-neutral-200">
                    Jim Green
                  </td>
                  <td className="whitespace-nowrap px-6 py-4 text-sm text-gray-800 dark:text-neutral-200">
                    27
                  </td>
                  <td className="whitespace-nowrap px-6 py-4 text-sm text-gray-800 dark:text-neutral-200">
                    London No. 1 Lake Park
                  </td>
                  <td className="whitespace-nowrap px-6 py-4 text-end text-sm font-medium">
                    <button
                      type="button"
                      className="inline-flex items-center gap-x-2 rounded-lg border border-transparent text-sm font-semibold text-blue-600 hover:text-blue-800 focus:text-blue-800 focus:outline-none disabled:pointer-events-none disabled:opacity-50 dark:text-blue-500 dark:hover:text-blue-400 dark:focus:text-blue-400"
                    >
                      Delete
                    </button>
                  </td>
                </tr>

                <tr>
                  <td className="whitespace-nowrap px-6 py-4 text-sm font-medium text-gray-800 dark:text-neutral-200">
                    Joe Black
                  </td>
                  <td className="whitespace-nowrap px-6 py-4 text-sm text-gray-800 dark:text-neutral-200">
                    31
                  </td>
                  <td className="whitespace-nowrap px-6 py-4 text-sm text-gray-800 dark:text-neutral-200">
                    Sidney No. 1 Lake Park
                  </td>
                  <td className="whitespace-nowrap px-6 py-4 text-end text-sm font-medium">
                    <button
                      type="button"
                      className="inline-flex items-center gap-x-2 rounded-lg border border-transparent text-sm font-semibold text-blue-600 hover:text-blue-800 focus:text-blue-800 focus:outline-none disabled:pointer-events-none disabled:opacity-50 dark:text-blue-500 dark:hover:text-blue-400 dark:focus:text-blue-400"
                    >
                      Delete
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Table;
